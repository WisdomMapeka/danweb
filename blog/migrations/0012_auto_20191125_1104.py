# Generated by Django 2.2.3 on 2019-11-25 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_home_page_hide_panel_statement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='category',
        ),
        migrations.AddField(
            model_name='tags',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='blog.Categories'),
        ),
    ]
