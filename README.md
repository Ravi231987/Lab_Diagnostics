Basic installations and command required to run the application in following order:
•	Install latest version of python3
•	Install Django with following commands, used as a web framework to implement the application
o	pip install Django
o	Use the following command  to check the version installed “python -m django –version”
o	Command to run the Django server “python manage.py run server”
•	Install scheduler crontab
o	Pip install Django-crontab
o	Make sure run this command every time CRONJOBS  is changed “python manage.py crontab add”
o	Use the following command to check active CRONJOBS  “python manage.py crontab show”
Following method has been used to implement the send the email by uploading CSV file 
•	Create CSV file to upload having  recipient’s emails, Sender email ID, Subject ,body 
•	








