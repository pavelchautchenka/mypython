# Generated by Django 5.0 on 2023-12-17 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hwork', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='mod_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]