# Generated by Django 2.2.3 on 2019-11-27 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20191127_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer_tags_heading_text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default="couldn't find what you are looking for, worry not. Try the tags below", max_length=600, null=True)),
            ],
            options={
                'db_table': 'footer_tags_heading_text',
            },
        ),
        migrations.CreateModel(
            name='Social_media_heading_text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Like Us On Social Media', max_length=200, null=True)),
            ],
            options={
                'db_table': 'social_media_heading_text',
            },
        ),
        migrations.CreateModel(
            name='Social_media_icons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Social media icons', max_length=200, null=True)),
                ('icon_img', models.ImageField(blank=True, null=True, upload_to='media/icons')),
            ],
            options={
                'db_table': 'social_media_icons',
            },
        ),
    ]
