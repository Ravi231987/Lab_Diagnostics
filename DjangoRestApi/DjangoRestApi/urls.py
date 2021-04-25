from django.conf.urls import url, include 
 
urlpatterns = [ 
    url(r'^', include('email_api.urls')),
]