# Generated by Django 3.0.5 on 2020-04-14 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20200413_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='date_pub',
            field=models.DateField(default=2003),
        ),
    ]
