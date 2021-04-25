from datetime import datetime, timedelta
from multiprocessing import Pool

from django.contrib import messages
from django.core.mail import send_mass_mail
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
import django

django.setup()
from email_api.models import DailyMailCount

total_mail_send = 0

# Send the mail asyncronously to target the performance,
def asyncSendMail(row, count):
    # To,From,Subject,Body
    mails = []
    col = row.split(",")
    to_email_ids = col[0].split("|")
    from_email = col[1]
    subject = col[2]
    body = col[3]
    from_password = col[4]
    print("info:", count - 1, " ", row)
    mails.append((subject, body, from_email, to_email_ids))
    send_mass_mail(mails, False, from_email, from_password)


import threading

total_mail_send = 0

# Callback Function for each thread to increment the TotalMailSend per CSV.
def incr_total_send_mails(self):
    global total_mail_send
    counter_lock = threading.Lock()
    with counter_lock:
        total_mail_send += 1
        value = total_mail_send
        print(value)

# Persist the TotalMailSend in Database per CSV.
def upsert_to_database(total_mail_send):
    now = datetime.now()
    list = DailyMailCount(datetime=now, count=total_mail_send).save()
    print("now =", now)


# POST API, to upload csv, and send bulk mail by parsing the CSV.
# Postman Url: http://127.0.0.1:8080/api/email_api/upload_csv, form-data, attach file.csv in body.
@api_view(['POST'])
def upload_csv(request):
    global total_mail_send
    total_mail_send = 0
    # print('request', request.FILES['file'])
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "this is not csv")
    data_set = csv_file.read().decode('utf-8')
    count = 0
    pool = Pool(processes=8)
    for row in data_set.split("\n"):
        count += 1
        if count == 1:
            continue
        print('count', count)
        pool.apply_async(asyncSendMail, (row, count), callback=incr_total_send_mails)
    print('hello done')
    pool.close()
    pool.join()
    upsert_to_database(total_mail_send)
    print('Total Mail Sent', total_mail_send)
    return JsonResponse({'message': 'CSV Uploaded Successfully'}, status=status.HTTP_200_OK)


# @api_view(['GET'])
# def daily_mail_stats(request):
#     # trigger at 9:00PM
#     now = datetime.now()
#     nowminusOne = datetime.today() - timedelta(days=1)
#     print(nowminusOne)
#     total_daily_mail_count = DailyMailCount.objects.filter(datetime__range=(nowminusOne, now))
#     total_mail_send_today=0
#     for items in total_daily_mail_count:
#         total_mail_send_today+=items.count
#     print(total_mail_send_today)
#     return JsonResponse({}, status=status.HTTP_200_OK)
