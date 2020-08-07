from django.contrib import admin
from . models import (Products, Categories, Home_Page, Tags, Icons, Benefit_listings, Trust_listings,
     Footer_tags_heading_text, Social_media_heading_text, Social_media_icons, 
     Messages_from_client)

# Register your models here.
admin.site.register(Home_Page)
# admin.site.register(Tags)
admin.site.register(Icons)
admin.site.register(Benefit_listings)
admin.site.register(Trust_listings)

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug', 'category_description')
    prepopulated_fields = {"slug": ("category_name",)}   
admin.site.register(Categories, CategoriesAdmin)

class TagsAdmin(admin.ModelAdmin):
    list_display = ('tag_name', 'slug')
    prepopulated_fields = {"slug": ("tag_name",)}   
admin.site.register(Tags, TagsAdmin)


class ProductsAdmin(admin.ModelAdmin):
    fields = ('product_name', 'slug', 'product_price',  'product_picture', ('category', 'product_tag'),  )
    list_display = ('product_name', 'category', 'product_tag')
    prepopulated_fields = {"slug": ("product_name",)}   
admin.site.register(Products, ProductsAdmin)

# admin.site.register(Products)
# admin.site.register(Categories)

admin.site.register(Footer_tags_heading_text)
admin.site.register(Social_media_heading_text)
admin.site.register(Social_media_icons)


class Messages_from_clientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'message')
admin.site.register(Messages_from_client, Messages_from_clientAdmin)




