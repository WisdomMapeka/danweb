# Generated by Django 2.2.3 on 2019-11-27 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20191125_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='tags',
            name='tag_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='slug',
            field=models.SlugField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tags',
            name='slug',
            field=models.SlugField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tags',
            name='tag_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
