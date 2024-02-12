from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
from .models import clss,student,teacher,att,regi,tsa
from django.views.decorators.cache import never_cache
from django.contrib.auth.hashers import check_password,make_password
from django.contrib.auth import update_session_auth_hash
from datetime import datetime,time,timedelta



# Create your views here.
@never_cache
def index(request):
    return render(request,'index.html')

              
@never_cache                          
def faculty(request,id):
    if(id[0]=='t' and request.user.is_authenticated and request.user.username==id):
        data=teacher.objects.get(tid=id)
        cls=clss.objects.filter(tid=id)
        return render(request,'faculty.html',{'data':data,'cls':cls})
    else:
        return redirect('index')
@never_cache                          
def stud(request,id):
    if(student.objects.filter(sid=id).exists() and request.user.is_authenticated and request.user.username==id):
        std=student.objects.get(sid=id)
        attd=att.objects.filter(sid=id)
        return render(request,'student.html',{'std':std,'attd':attd})
    else:
        return redirect('index')
          
def logout(request):
    auth.logout(request)
    return redirect('index')           
@never_cache 
def css(request,id):

    if(request.user.is_authenticated and clss.objects.filter(sclass=id,tid=request.user.username).exists()):
        std=student.objects.filter(sclass=id)
        sub=teacher.objects.get(tid=request.user.username).sub
        return render(request,'clss.html',{'std':std,'id':id ,'sub':sub})
    
def calculate(request):
    if(request.method=="POST" and request.user.is_authenticated and str(request.user.username[0].lower())=='t' ):
        c=request.POST['class']
        p=request.POST['period']
        std=student.objects.filter(sclass=c)
        sb=teacher.objects.get(tid=request.user.username)
        if(not tsa.objects.filter(tid=request.user.username,period=p,sub=request.POST['sub'],sclass=c,tm=datetime.now().date()).exists()):
         for st in std:
           ast=att.objects.get(sub=sb.sub,sid=st.sid)
           if(request.POST.get(st.sid,'')):
               x=ast.sub_attended
               ast.sub_attended=x+1
               ast.save()
               r=regi.objects.create(sid=st.sid,sub=request.POST['sub'],tm=datetime.now().date(),period=p)
               r.save()
           y=ast.sub_total
           ast.sub_total=y+1
           ast.save()
         jj=tsa.objects.create(tid=request.user.username,sub=request.POST['sub'],tm=datetime.now(),period=request.POST['period'],sclass=c)
         jj.save()
         return redirect('faculty/'+request.user.username) 
        else:
            messages.info(request,'Attendence Already Taken')
            return redirect('faculty/class/'+c)            
    else:
        return redirect('index')
    
def login(request):
    if(request.method=="POST"):
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if(user is not None and str(username[0].lower())=='r'):
            auth.login(request,user)
            return redirect('student/'+username)
        elif(user is not None and str(username[0].lower())=='t'):
              auth.login(request,user)
              return redirect('faculty/'+username)
        elif(user is not None and str(username[0].lower())=='s'):
            auth.login(request,user)
            return redirect('dean/'+username) 
        else:
             messages.info(request,'user not found')
             return redirect('index')
    else:
        return redirect('index')    

def passwd(request):
  if request.user.is_authenticated:
    if request.method=="POST":
          cpass=request.POST['cpass']
          npass=request.POST['npass']
          cnpass=request.POST['cnpass']
          user=auth.authenticate(username=request.user.username,password=cpass)
          if(user is not None):
              user=User.objects.get(username=request.user.username)
              if(str(npass)!=str(cnpass)):
                messages.info(request,'password not matched')
                return redirect('passwd')  
              elif(check_password(npass,user.password)):
                   messages.info(request,'same as previous password')
                   return redirect('passwd') 
              else:
                  user.set_password(cnpass)
                  user.save()
                  update_session_auth_hash(request, user)  
                  messages.info(request,'password changed successfully')
                  return redirect('passwd')                   
          else:
              messages.info(request,'user not found')
              return redirect('passwd')
        
    else:
       return render(request,'passwd.html')
  else:
      return redirect('index')  
  

    
def reg(request):
    if(request.user.is_authenticated and str(request.user.username[0].lower())=='t'):
        if(request.method=="POST"):
            cl=request.POST['class']
            cls=student.objects.filter(sclass=cl)
            s=teacher.objects.get(tid=request.user.username).sub
            fro=request.POST.get('from','')
            fro1= datetime.strptime(fro, '%Y-%m-%d').date()
            to=request.POST.get('to','')
            to1= datetime.strptime(to, '%Y-%m-%d').date()
            ts=tsa.objects.filter(tm__range=(fro1,to1),tid=request.user.username,sub=s,sclass=cl)
            l=[]
            for cl in cls:
                ll=[]
                for tt in ts:
                    if(regi.objects.filter(sid=cl.sid,sub=s,tm=tt.tm,period=tt.period).exists()):
                       ll.append('P') 
                    else:
                        ll.append('A')
                l.append((cl,ll))

            return render(request,'register.html',{'ts':ts,'l':l})
        else:
         c=clss.objects.filter(tid=request.user.username) 
         return render(request,'regform.html',{'c':c})

    else:
        return redirect('index')

def dean(request,id):
    if(id[0]=='s' and request.user.is_authenticated and request.user.username==id):
       
        return render(request,'dean.html')
    else:
        return redirect('index')
    

def addstud(request):
    if(request.user.is_authenticated and request.user.username[0]=='s'):
        if(request.method=="POST"):
           roll=request.POST.get('roll','')
           sid=request.POST.get('sid','')
           sname=request.POST.get('sname','')
           sclass=request.POST.get('sclass','')
           dep=request.POST.get('dep','')
           year=request.POST.get('year','')
           up=request.POST.get('update','')
           password='skjani314@A'
           password=make_password(password)
           if(student.objects.filter(sid=sid).exists() and up):
              s=student.objects.get(sid=sid)
              aa=att.objects.get(sid=sid)
              for a in aa:
                  a.sclass=sclass
              s.roll=roll
              s.sid=sid
              s.sname=sname
              s.sclass=sclass
              s.dep=dep
              s.year=year
              s.save()
              
              messages.info(request,"updated successfully")
              return redirect('addstud')
           elif(student.objects.filter(sid=sid).exists() and not up):
                messages.info(request,"user already exists")
                return redirect('addstud')
           elif( not student.objects.filter(sid=sid).exists() and up):
               messages.info(request,"user not found")
               return redirect('edit_class')
           else:
              u= User.objects.create(username=sid,password=password)
              u.save()
              s=student.objects.create(sid=sid,roll=roll,sname=sname,sclass=sclass,dep=dep,year=year)
              s.save()
              cls=clss.objects.filter(sclass=sclass)
              for i in cls:
                  at=att.objects.create(sid=sid,sclass=sclass,sub=i.sub,sub_total=0,sub_attended=0)
                  at.save()
              messages.info(request,"Added Successfully")
              return redirect('addstud')
        else:
          return render(request,'addstud.html')
        

def editreg(request):
    if (request.user.is_authenticated and request.user.username[0]=='t'):
         if(request.method=="POST"):
             per=request.POST.get('period','')
             da=request.POST.get('pov','')
             cl=request.POST.get('class','')
             ab=request.POST.get('ab','')
             pr=request.POST.get('pr','')
             sid=request.POST.get('sid','')
             sub=teacher.objects.get(tid=request.user.username).sub
             r=regi.objects.filter(sid=sid,sub=sub,tm=da,period=per)
             da1=datetime.strptime(da, '%Y-%m-%d').date()
             at=att.objects.get(sid=sid,sclass=cl,sub=sub)
             if(da1+timedelta(days=1)>=datetime.today().date() and ab!=pr and clss.objects.filter(tid=request.user.username,sclass=cl,sub=sub).exists()):
                if(ab and r.exists()):
                    r.delete()
                    x=at.sub_attended
                    at.sub_attended=x-1
                    at.save()
                    messages.info(request,"update succesfully")
                    return redirect('editreg')
                elif(pr and not r.exists()):
                    r1=regi.objects.create(sid=sid,sub=sub,tm=da1,period=per)
                    r1.save()
                    y=at.sub_attended
                    at.sub_attended=y+1
                    at.save()
                    messages.info(request,"update succesfully")
                    return redirect('editreg')
                else:
                    messages.info(request,"NO NEED OF UPDATE")
                    return redirect('editreg')
             else:
               messages.info(request,"cant update")
               return redirect('editreg')

         else:
          c=clss.objects.filter(tid=request.user.username) 
          return render(request,'editreg.html',{'c':c})
    else:
        return redirect('index')

def editclass(request):
    if(request.user.is_authenticated and request.user.username[0]=='s'):
        if(request.method=="POST"):
          tid=request.POST['tid']
          sclass=request.POST['sclass']
          sub=request.POST['sub']
          up=request.POST.get('update','')
          r=clss.objects.filter(sclass=sclass,sub=sub)
          if(r.exists() and up):
              r.tid=tid
              r.save()
              messages.info(request,"updated succesfully")
              return redirect('edit_class')
          elif(r.exists() and not up):
               messages.info(request,"user already exists")
               return redirect('edit_class')
          elif( not r.exists() and up):
               messages.info(request,"user not found")
               return redirect('edit_class')
          else:
            sl=clss.objects.create(tid=tid,sclass=sclass,sub=sub)
            sl.save()
            cls=student.objects.filter(sclass=sclass)
            t=teacher.objects.get(tid=tid)
            t.sub=sub
            t.save()
            for cl in cls:
               at=att.objects.create(sid=cl.sid,sclass=sclass,sub=sub,sub_total=0,sub_attended=0)
               at.save()
            messages.info(request,"Added Successfully")
            return redirect('edit_class')
        
        else:
            return render(request,'editclass.html')

    else:
        return redirect('index')
    
def editteacher(request):
    if(request.user.is_authenticated and request.user.username[0]=='s'):
        if(request.method=="POST"):
          tid=request.POST.get('tid','')
          tname=request.POST.get('tname','')
          sub=request.POST.get('sub','')
          dep=request.POST.get('dep','')
          up=request.POST.get('update','')
          if(teacher.objects.filter(tid=tid).exists() and up):
                t=teacher.objects.get(tid=tid)
                t.tname=tname
                t.save()
                messages.info(request,"updated succesfully")
                return redirect('edit_teacher')
          elif(teacher.objects.filter(tid=tid).exists() and not up):
            messages.info(request,"user already exists")
            return redirect('edit_teacher') 
          elif( not teacher.objects.filter(tid=tid).exists() and up):
               messages.info(request,"user not found")
               return redirect('edit_class')
          else:   
            password='skjani314@A'
            password=make_password(password)
            u=User.objects.create(username=tid,password=password)
            u.save()
            t=teacher.objects.create(tid=tid,tname=tname,sub=sub,dep=dep)
            t.save()
            messages.info(request,"Added succesfully")
            return redirect('edit_teacher')
        else:
            return render(request,'editteacher.html')

    else:
        return redirect('index')
    

def contact(request):
     return render(request,'contact.html')