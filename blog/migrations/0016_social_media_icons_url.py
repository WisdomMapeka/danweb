# Generated by Django 2.2.3 on 2019-11-28 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_footer_tags_heading_text_social_media_heading_text_social_media_icons'),
    ]

    operations = [
        migrations.AddField(
            model_name='social_media_icons',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
