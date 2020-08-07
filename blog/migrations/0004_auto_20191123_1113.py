# Generated by Django 2.2.3 on 2019-11-23 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191123_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='icons',
            name='call_icon',
        ),
        migrations.RemoveField(
            model_name='icons',
            name='direct_message_icon',
        ),
        migrations.RemoveField(
            model_name='icons',
            name='email_icon',
        ),
        migrations.RemoveField(
            model_name='icons',
            name='menu_button_icon',
        ),
        migrations.RemoveField(
            model_name='icons',
            name='whatsapp_icon',
        ),
        migrations.AlterField(
            model_name='icons',
            name='drop_down_arrow_icon',
            field=models.ImageField(blank=True, null=True, upload_to='media/icons'),
        ),
        migrations.AlterField(
            model_name='icons',
            name='name',
            field=models.CharField(blank=True, default='Icons', max_length=200, null=True),
        ),
    ]
