# Generated by Django 2.2.3 on 2019-11-23 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=300, null=True)),
                ('category_description', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=300, null=True)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(blank=True, max_length=300, null=True)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True)),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.AlterField(
            model_name='home_page',
            name='benefit_listing_heading',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='home_page',
            name='trust_listing_heading',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=300, null=True)),
                ('product_price', models.CharField(blank=True, max_length=20, null=True)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True)),
                ('product_picture', models.ImageField(upload_to='media/products')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Categories')),
                ('product_tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Tags')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
