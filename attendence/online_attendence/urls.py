from django.urls import path
from django.contrib.auth.views import LogoutView
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('faculty/<str:id>',views.faculty,name='faculty'),
    path('student/<str:id>',views.stud,name='student'),
    path('logout',views.logout,name='logout'),
    path('faculty/class/<str:id>',views.css,name='class'),
    path('calculate',views.calculate,name='calculate'),
    path('passwd',views.passwd,name='passwd'),
    path('faculty/myregister/',views.reg,name='reg'),
    path('dean/<str:id>',views.dean,name='dean'),
    path('addstud',views.addstud,name='addstud'),
    path('editreg',views.editreg,name='editreg'),
    path('edit_class',views.editclass,name='edit_class'),
    path('edit_teacher',views.editteacher,name='edit_teacher'),


    



]
