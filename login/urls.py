
from django.conf.urls import include,url
from .views import *

urlpatterns = [
   
    url(r'^$',login,name='log'),
    #url(r'^nextpage/$',nxt),
    
    url(r'^auth_check/$',auth_view,name='check'),
    url(r'^logout/$',logout),
    url(r'^logged_in/$',loggedin),
    url(r'^invalid/$',invalid_login),
    url(r'^register/$',register_user,name='register'),
    # url(r'^register_success/$',register_success)
    
]




