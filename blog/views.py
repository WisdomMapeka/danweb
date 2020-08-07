from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
import datetime
from django.urls import reverse
from django.contrib import messages
from . models import (Products, Home_Page, Benefit_listings, 
                     Trust_listings, Icons, Tags, Categories, 
                     Footer_tags_heading_text, Social_media_heading_text,
                     Social_media_icons, Messages_from_client)

from . forms import Messages_from_client_form

# Create your views here.

def home(request):
    year = datetime.date.today().year
    social_media_icons = Social_media_icons.objects.all()
    social_media_heading_text = Social_media_heading_text.objects.all().first()
    footer_tags_heading_text = Footer_tags_heading_text.objects.all().first()
    menu_button = get_object_or_404(Icons, name="menu button")
    benefit_listings = Benefit_listings.objects.all()
    home_page = Home_Page.objects.all().first()
    trust_listings = Trust_listings.objects.all().first()
    recent_products = Products.objects.all().order_by("id").reverse()[:4]
    cat1 = []
    cat2 = []
    cat3 = []
    cat4 = []

    try:
        cat1 = Categories.objects.all()[0]
        cat2 = Categories.objects.all()[1]
        cat3 = Categories.objects.all()[2]
        cat4 = Categories.objects.all()[3]
    except:
        pass

    return render(request, "blog/home.html", 
        {"home_page":home_page, "benefit_listings":benefit_listings, "trust_listings":trust_listings, "menu_button":menu_button,
         "cat1":cat1, "cat2":cat2, "cat3":cat3, "cat4":cat4,
         "recent_products":recent_products, "footer_tags_heading_text":footer_tags_heading_text,
         "social_media_heading_text":social_media_heading_text,
         "social_media_icons":social_media_icons, "year":year})


def products(request, slug):
    year = datetime.date.today().year
    social_media_icons = Social_media_icons.objects.all()
    social_media_heading_text = Social_media_heading_text.objects.all().first()
    footer_tags_heading_text = Footer_tags_heading_text.objects.all().first()
    menu_button = get_object_or_404(Icons, name="menu button")
    benefit_listings = Benefit_listings.objects.all()
    home_page = Home_Page.objects.all().first()
    trust_listings = Trust_listings.objects.all().first()
    first_product_from_selected_category = " "
    all_products_from_selected_category = get_object_or_404(Categories, slug=slug)

    cat1 = []
    cat2 = []
    cat3 = []
    cat4 = []

    try:
        cat1 = Categories.objects.all()[0]
        cat2 = Categories.objects.all()[1]
        cat3 = Categories.objects.all()[2]
        cat4 = Categories.objects.all()[3]
        first_product_from_selected_category = get_object_or_404(Categories, slug=slug).products_set.all()[0]
    except:
        pass

    return render(request, "blog/products.html", 
        {"home_page":home_page, "benefit_listings":benefit_listings, "trust_listings":trust_listings, "menu_button":menu_button,
         "cat1":cat1, "cat2":cat2, "cat3":cat3, "cat4":cat4, "first_product_from_selected_category":first_product_from_selected_category,
         "all_products_from_selected_category":all_products_from_selected_category,
         "footer_tags_heading_text":footer_tags_heading_text,
         "social_media_heading_text":social_media_heading_text,
         "social_media_icons":social_media_icons, "year":year})


def tags(request, slug):
    year = datetime.date.today().year
    social_media_icons = Social_media_icons.objects.all()
    social_media_heading_text = Social_media_heading_text.objects.all().first()
    footer_tags_heading_text = Footer_tags_heading_text.objects.all().first()
    menu_button = get_object_or_404(Icons, name="menu button")
    benefit_listings = Benefit_listings.objects.all()
    home_page = Home_Page.objects.all().first()
    trust_listings = Trust_listings.objects.all().first()
    first_product_from_selected_tags = " "
    all_products_from_selected_tags = get_object_or_404(Tags, slug=slug)

    cat1 = []
    cat2 = []
    cat3 = []
    cat4 = []

    try:
        cat1 = Categories.objects.all()[0]
        cat2 = Categories.objects.all()[1]
        cat3 = Categories.objects.all()[2]
        cat4 = Categories.objects.all()[3]
        first_product_from_selected_tags = get_object_or_404(Tags, slug=slug).products_set.all()[0]
    except:
        pass

    return render(request, "blog/tags.html", 
        {"home_page":home_page, "benefit_listings":benefit_listings, "trust_listings":trust_listings, "menu_button":menu_button,
         "cat1":cat1, "cat2":cat2, "cat3":cat3, "cat4":cat4, "first_product_from_selected_tags":first_product_from_selected_tags,
         "all_products_from_selected_tags":all_products_from_selected_tags,
         "footer_tags_heading_text":footer_tags_heading_text,
         "social_media_heading_text":social_media_heading_text,
         "social_media_icons":social_media_icons,  "year":year})


def client_message(request):

    year = datetime.date.today().year
    social_media_icons = Social_media_icons.objects.all()
    social_media_heading_text = Social_media_heading_text.objects.all().first()
    footer_tags_heading_text = Footer_tags_heading_text.objects.all().first()
    menu_button = get_object_or_404(Icons, name="menu button")
    home_page = Home_Page.objects.all().first()

    cat1 = []
    cat2 = []
    cat3 = []
    cat4 = []

    try:
        cat1 = Categories.objects.all()[0]
        cat2 = Categories.objects.all()[1]
        cat3 = Categories.objects.all()[2]
        cat4 = Categories.objects.all()[3]
    except:
        pass


    if request.method == "GET":
        form = Messages_from_client_form()
    else:
        form = Messages_from_client_form(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            number = form.cleaned_data["number"]
            message = form.cleaned_data["message"]
            client_mess = Messages_from_client(name=name, email=email, phone_number=number, message=message)
            client_mess.save()
            messages.add_message(request, messages.SUCCESS, "Your Message Was sent. Thank You")
            return HttpResponseRedirect(reverse("blog:client_message"))
    return render(request, "blog/client_message.html", {"form":form,
        "home_page":home_page,  "menu_button":menu_button,
         "cat1":cat1, "cat2":cat2, "cat3":cat3, "cat4":cat4,
         "footer_tags_heading_text":footer_tags_heading_text,
         "social_media_heading_text":social_media_heading_text,
         "social_media_icons":social_media_icons, "year":year})

        
