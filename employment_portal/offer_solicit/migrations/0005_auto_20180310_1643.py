# Generated by Django 2.0.2 on 2018-03-10 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer_solicit', '0004_merge_20180310_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer_invitation',
            name='uuid',
            field=models.CharField(default='RPBMH', max_length=5, primary_key=True, serialize=False),
        ),
    ]
