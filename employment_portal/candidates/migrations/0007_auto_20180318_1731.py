# Generated by Django 2.0.2 on 2018-03-18 22:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0006_auto_20180318_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='date_of_birth',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 3, 18, 17, 31, 36, 873408)),
        ),
    ]
