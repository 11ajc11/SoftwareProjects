# Generated by Django 2.0.2 on 2018-03-18 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer_solicit', '0019_auto_20180316_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer_invitation',
            name='uuid',
            field=models.CharField(default='GBTMP', max_length=5, primary_key=True, serialize=False),
        ),
    ]
