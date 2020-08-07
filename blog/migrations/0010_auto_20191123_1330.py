# Generated by Django 2.2.3 on 2019-11-23 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20191123_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='icons',
            name='drop_down_arrow_icon',
        ),
        migrations.AddField(
            model_name='icons',
            name='icon_img',
            field=models.ImageField(blank=True, help_text='The following names should be used as icon names, menu button, arrow down dropdown, whatsapp icon, call icon, email icon, direct message icon ', null=True, upload_to='media/icons'),
        ),
    ]
