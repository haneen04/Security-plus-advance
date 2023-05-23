from django.urls import path
from . import views 


urlpatterns = [
    path('',views.loginpage, name='login'),
    path('logout/',views.logoutUser, name='logout'),
    
    path('statics/',views.Statics, name='Statics'),
    path('add_profile/',views.add_profile, name='Add_Profile'),
    path('add_camera/',views.add_camera, name='Add_Camera'),
]