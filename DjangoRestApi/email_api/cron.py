from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from DjangoRestApi.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
from email_api.models import DailyMailCount
import smtplib
from datetime import date

#
# Method is used to send the daily mail count from 9PM of yesterday to today 9:00 PM,
# and this job will trigger at 9:00PM each day
def daily_mail_stats():
    print('my_cron_job starts')
    now = datetime.now()
    nowminusOne = datetime.today() - timedelta(days=1)
    print(nowminusOne)
    total_daily_mail_count = DailyMailCount.objects.filter(datetime__range=(nowminusOne, now))
    total_mail_send_today=0
    for items in total_daily_mail_count:
        total_mail_send_today+=items.count
    print('mail_stats', total_mail_send_today)
    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    msg = MIMEMultipart()
    # setup the parameters of the message
    msg['From']=EMAIL_HOST_USER
    msg['To']='ravi.lalwani2187@gmail.com'
    msg['Subject']="Mail Stats for "+ str(date.today())
    body='Hi Admin, Total Mails Send Today: '+str(total_mail_send_today)
    msg.attach(MIMEText(body,'plain'))
    s.send_message(msg)
    del msg
    # Terminate the SMTP session and close the connection
    s.quit()
    print('my_cron_job ends')

