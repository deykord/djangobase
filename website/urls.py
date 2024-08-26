
from django.urls import path
from website.views import *
app_name = 'website'
urlpatterns = [
    path('',index_view ),
    path('index.html',index_view ,name='home'),
    path('about', about_view,name='about' ),
    path('elements.html', elements_view ,name='elements'),
    path('contact.html', contact_view , name='contact' )
]
