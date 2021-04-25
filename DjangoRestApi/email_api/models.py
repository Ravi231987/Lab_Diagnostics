from django.db import models
from datetime import datetime

class DailyMailCount(models.Model):
    datetime = models.DateTimeField(default=datetime.now, blank=True)
    count = models.DecimalField(default=0,max_digits=1000,decimal_places=0)



