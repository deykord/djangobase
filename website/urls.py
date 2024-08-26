
from django.urls import path
from website.views import *

urlpatterns = [
    path('',index_view ),
    path('index.html',index_view ),
    path('about.html', about_view ),
    path('contact.html', contact_view )
]
