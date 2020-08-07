from django.db import models
from django.urls import reverse

# Create your models here.

class Home_Page(models.Model):
    header_background_img = models.ImageField(upload_to = "media/home_page", help_text="Try Out Different Images until You Find One That Fit well")
    site_theme = models.CharField(max_length = 400, blank=True, null=True, default="Site theme", help_text="Max 400 Characters")
    site_description = models.CharField(max_length=600, blank=True, null=True, help_text="max 600 Characters")
    call_number = models.CharField(max_length=20, blank=True, null=True, help_text="Max 20 Characters")
    whatsapp_number = models.CharField(max_length=20, blank=True, null=True, help_text= "Max 20 Characters ")
    email = models.EmailField(max_length=100, blank=True, null=True, help_text="Max 100 Characters")
    call_to_action_statement = models.CharField(max_length=600, blank=True, null=True, help_text="Max 600 Characters ")
    hide_panel_statement = models.CharField(max_length=600, blank=True, null=True, help_text="Max 600 Characters ")
    # direct_message = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.site_theme

    class Meta:
        db_table = "home_page"
        verbose_name = "Home Page"
        verbose_name_plural = "Home Page"

class Benefit_listings(models.Model):
    benefit_listing_heading = models.CharField(max_length=300, blank=True, null=True, help_text="Max 300 Characters")
    benefit_listing_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.benefit_listing_heading

    class Meta:
        db_table="benefit_listings"
        verbose_name = "Benefit listing"


class Trust_listings(models.Model):
    trust_listing_heading = models.CharField(max_length=300, blank=True, null=True, help_text="Max 300 Characters")
    trust_listing_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.trust_listing_heading

    class Meta:
        db_table="trust_listings"
        verbose_name = "Trust listing"



class Categories(models.Model):
    category_name =  models.CharField(max_length=300, blank=True, null=True, help_text="Max 300 Characters")
    category_description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=300, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('blog:products', args=[str(self.slug)])


    def __str__(self):
        return self.category_name

    class Meta:
        db_table="categories"
        verbose_name = "Categorie"

# Each Tag should have a coresponding category. Each Tag should be displayed based on the category it belongs to
class Tags(models.Model):
    category = models.ManyToManyField(Categories,  blank=True)
    tag_name = models.CharField(max_length=30, blank=True, null=True, help_text="Max 30 Characters")
    slug = models.SlugField(max_length=30, blank=True, null=True, help_text="Max 30 Characters")
    tag_description = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('blog:tags', args=[str(self.slug)])


    def __str__(self):
        return self.tag_name

    class Meta:
        db_table="tags"
        verbose_name = "Tag"

class Products(models.Model):
    product_name = models.CharField(max_length=30, blank=True, null=True, help_text="Max 30 Characters")
    product_price = models.CharField(max_length=20, blank=True, null=True, help_text="Max 20 Characters")
    product_tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=30, blank=True, null=True, help_text="Max 30 Characters")
    product_picture = models.ImageField(upload_to="media/products", blank=True, null=True)
    category = models.ForeignKey(Categories, on_delete = models.CASCADE, blank=True, null=True)



    def __str__(self):
        return self.product_name

    class Meta:
        db_table="products"
        verbose_name = "Product"

# DIRECT MESSAGE FORM. This is linked to a message form
class Messages_from_client(models.Model):
    name = models.CharField(max_length=600, null=True, blank=True , help_text="Max 600 Characters")
    email =  models.EmailField(max_length=600, null=True, blank=True , help_text="Max 600 Characters")
    phone_number = models.CharField(max_length=600, blank=True, null=True , help_text="Max 600 Characters")
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table="messages_from_clients"
        verbose_name = "Messages From Client"




# FOOTER MODELS============================================================


class Icons(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, default="Icons", help_text="Max 200 Characters")
    icon_img = models.ImageField(upload_to="media/icons", blank=True, null=True, 
        help_text="The following names should be used as icon names, menu button, arrow down dropdown, whatsapp icon, call icon, email icon, direct message icon ")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "icons"
        verbose_name = "Menu Icon"


class Social_media_icons(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, default="Social media icons", help_text="Max 200 Characters")
    icon_img = models.ImageField(upload_to="media/icons", blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "social_media_icons"
        verbose_name = "Social Media Icon"

class Social_media_heading_text(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, default="Follow Us", help_text="Max 200 Characters")

    def __str__(self):
        return self.name

    class Meta(object):
        db_table="social_media_heading_text"
        verbose_name = "Social Media Heading Text"
            

class Footer_tags_heading_text(models.Model):
    name = models.CharField(max_length=600, blank=True, null=True, help_text="Max 600 Characters",
        default="couldn't find what you are looking for, worry not. Try the tags below")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "footer_tags_heading_text"
        verbose_name = "Footer Tags Heading Text"


# FOOTER MODELS END============================================








