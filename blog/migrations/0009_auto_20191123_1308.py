# Generated by Django 2.2.3 on 2019-11-23 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20191123_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trust_listings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trust_listing_heading', models.CharField(blank=True, max_length=300, null=True)),
                ('trust_listing_description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'trust_listings',
            },
        ),
        migrations.RemoveField(
            model_name='home_page',
            name='trust_listing_description',
        ),
        migrations.RemoveField(
            model_name='home_page',
            name='trust_listing_heading',
        ),
    ]
