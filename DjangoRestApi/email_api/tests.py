from datetime import datetime, timedelta


def daily_mail_stats():
    #trigger at 9:00PM
    now = datetime.now()
    now = datetime.today() - timedelta(days=1)
    now = now.replace(hour=21)
    print(now)
    #DailyMailCount.objects.filter(datetime>=now-1)

daily_mail_stats()