# Basic set up and cmd are required for Bulk Mail sender:

> Install latest version of python3

> _Install Django with following commands, used as a web framework to implement the application_:

>     pip install Django
 
>     Use the following command  to check the version installed “python -m django –version” 
    
>     Command to run the Django server “python manage.py run server 8080”
   
>  	_Install scheduler crontab_:
     
>       Pip install Django-crontab
       
>       Make sure run this command every time CRONJOBS is changed or newly added “python manage.py crontab add”

>       Use the following command to check active CRONJOBS  “python manage.py crontab show”
       

#  Postman Url and Method to Implement bulk email by uploading CSV file:

> _Create CSV file to upload having  [recipient’s emails, Sender email ID, Subject ,body,Password]_

>  _POST API, to upload csv, and send bulk mail by parsing the CSV._
  
>       Postman Url: "http://127.0.0.1:8080/api/email_api/upload_csv", form-data, attach file.csv in body.

> **Below Methods are used :**

>       Method name "def upload_csv" to send the email in asynchronous mode
       
>       Method name "incr_total_send_mails" Callback Function for each thread to increment the TotalMailSend per CSV
       
>       Method name "def upsert_to_database" Persist the TotalMailSend in Database per CSV, which used to calculate the total number email send every day at 9PM
>       

# Cron job is created to send the email 

> crop.py is the python script to send the email to admin every day at 9PM, by calculating the count stored in DBSqlite for last 24 hours(1 day).

# DBSqlite is used as database to store the stats of the email send by uploading the csv having attribute below 

> **count** : _to stored the number of successful email send by per csv_

> **DataTime** : _to store the time of successful email send by per csv_

> _"Database object defination can be found under model.py"_
> 
# Below configuartion has been added to setting.py

 > **Email**

 >EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'

 >EMAIL_HOST = 'smtp.gmail.com'

 >EMAIL_USE_TLS = True

 >EMAIL_PORT = 587

 > **Auth User Email Id and Password should be configured, to send the mail.**

 >EMAIL_HOST_USER = 'host_mail_id'

 >EMAIL_HOST_PASSWORD = 'host_password*'


> **Cron settings to call the cron jobs at 9PM to send the notification to Admin Everyday**
>
CRONJOBS = [
    ('* 21 * * *', 'email_api.cron.daily_mail_stats', '>> /Users/glalwani/BitBucket/django-rest-api-master/DjangoRestApi/Log.log')
]
>
**Thank you have a Great Day**




