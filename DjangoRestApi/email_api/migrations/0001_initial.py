# Generated by Django 3.2 on 2021-04-25 18:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyMailCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('count', models.DecimalField(decimal_places=0, default=0, max_digits=1000)),
            ],
        ),
    ]
