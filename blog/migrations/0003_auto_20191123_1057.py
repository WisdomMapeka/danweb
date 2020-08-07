# Generated by Django 2.2.3 on 2019-11-23 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191123_0920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('drop_down_arrow_icon', models.ImageField(blank=True, help_text='icon name should always be drop-down-arrow-icon', null=True, upload_to='media/icons')),
                ('menu_button_icon', models.ImageField(blank=True, help_text='icon name should always be menu-button-icon', null=True, upload_to='media/icons')),
                ('whatsapp_icon', models.ImageField(blank=True, help_text='icon name should always be whatsapp-icon', null=True, upload_to='media/icons')),
                ('call_icon', models.ImageField(blank=True, help_text='icon name should always be call-icon', null=True, upload_to='media/icons')),
                ('email_icon', models.ImageField(blank=True, help_text='icon name should always be email-icon', null=True, upload_to='media/icons')),
                ('direct_message_icon', models.ImageField(blank=True, help_text='icon name should always be direct-message-icon', null=True, upload_to='media/icons')),
            ],
            options={
                'db_table': 'icons',
            },
        ),
        migrations.AlterField(
            model_name='categories',
            name='category_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='home_page',
            name='benefit_listing_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='home_page',
            name='direct_message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='home_page',
            name='trust_listing_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_picture',
            field=models.ImageField(blank=True, null=True, upload_to='media/products'),
        ),
    ]