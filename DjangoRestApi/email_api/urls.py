from django.conf.urls import url 
from email_api import views
 
urlpatterns = [ 
    url('api/email_api/upload_csv', views.upload_csv),
    #url('api/email_api/daily_mail_stats', views.daily_mail_stats)
]