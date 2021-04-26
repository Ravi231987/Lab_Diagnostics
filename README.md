# Basic set up and cmd are required for Bulk Mail sender email:

> Install latest version of python3

> _Install Django with following commands, used as a web framework to implement the application_:

>     pip install Django
 
>     Use the following command  to check the version installed “python -m django –version” 
    
>     Command to run the Django server “python manage.py run server”
   
>  	_Install scheduler crontab_:
     
>       Pip install Django-crontab
       
>       Make sure run this command every time CRONJOBS  is changed “python manage.py crontab add”

>       Use the following command to check active CRONJOBS  “python manage.py crontab show”
       

# Methods to Implement bulk email by uploading CSV file:

> _Create CSV file to upload having  recipient’s emails, Sender email ID, Subject ,body_

>  _POST API, to upload csv, and send bulk mail by parsing the CSV._
  
>       Postman Url: http://127.0.0.1:8080/api/email_api/upload_csv, form-data, attach file.csv in body.

>       Method name "def upload_csv" to send the email in asynchronous mode
       
>       Method name "incr_total_send_mails" Callback Function for each thread to increment the TotalMailSend per CSV
       
>       Method name "def upsert_to_database" Persist the TotalMailSend in Database per CSV, which used to calculate the total number email send every day at 9PM
>       

# Cron job is created to send the email 

> crop.py is the python script to send the email to admin every day at 9PM, by calculating the count stored in DBSqlite for last 24 hours(1 day).

# DBSqlite is used as database to store the stats of the email send by uploading the csv having attribute below 
> count : to stored the number of sucessful email send by per csv
> DataTime : 
      




