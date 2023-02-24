from django.urls import path
from .views import *
#http://127.0.0.1:8000/hms/ =base url to go to hms's app

urlpatterns = [
    path('home/',view_home, name='home'),
    path('about/',view_about,name='about'),
    path('timeline/',view_timeline,name='timeline'),
    path('healths/',view_healthspecialist,name='healths'),
    path('testimonials/',view_testimonials,name='testimonials'),
    path('booking/',view_booking,name='booking'),
    path('contacts/',view_contact,name='contact'),
    path('register/',view_registeration,name='register'),
    path('login/',view_login,name='login'),
    path('logout/', view_logout,name='logout'),
    
]