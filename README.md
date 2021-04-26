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

> Create CSV file to upload having  recipient’s emails, Sender email ID, Subject ,body 


