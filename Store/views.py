from django.shortcuts import render, redirect, get_object_or_404
from .models import AllProduct, Contact_company, Hotdealscountdown, Cartitem, Cart
from datetime import timedelta
from django.utils import timezone
from django.db import models
from .forms import SubscribersForm 
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q

# Create your views here.

# View for Homepage

def Index(request, subcategory=None):
    '''
    1-Getting new products created or updated withing last 30 days
    2-Getting top 26 selling products
    3-Getting contact info of a company
    '''

    # Calculating days
    thirty_days_ago = timezone.now() - timedelta(days=30)

    # Filtering new products younger than 30 days
    new_products = AllProduct.objects.filter(subcategory='Laptops', created_at__gte=thirty_days_ago)

    # Top selling products
    top_selling_products = AllProduct.objects.order_by('-sales')[:26]

    # Getting Contact Info of a Company
    All_contacts = Contact_company.objects.first()  # Assuming there's only one contact info entry

    # Adding discount percentage to each product of new_products

    for product in new_products:
        if product.new_price < product.old_price:
            discount_percentage = ((product.old_price - product.new_price) / product.old_price) * 100
            product.discount_percentage = round(discount_percentage, 2) # Stores calculated discount percentage with 2 decimal places
        else:
            product.discount_percentage = "No Offers"


    # Adding discount percentage to each product of top_selling_products

    for topselling in top_selling_products:
        if topselling.new_price < topselling.old_price:
            discount_percentage = ((topselling.old_price - topselling.new_price) / topselling.old_price) * 100
            topselling.discount_percentage = round(discount_percentage, 2) # Stores calculated discount percentage with 2 decimal places
        else:
            topselling.discount_percentage = "No Offers"
    

    # Hot Deals: Countdown Timer view

    countdown = Hotdealscountdown.objects.last() # Get the last countdown timer

    if countdown:
        now = timezone.now()
        time_left = countdown.end_date_time - now
        if time_left.total_seconds() > 0:
            days = time_left.days
            hours, remainder = divmod(time_left.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
        else:
            days, hours, minutes, seconds = 0, 0, 0, 0

    else:
        days, hours, minutes, seconds = 0, 0, 0, 0
 

    # context dictionary

    context = {'new_products':new_products, 
               'top_selling_products':top_selling_products, 
               'All_contacts':All_contacts,
               'countdown':countdown, 
               'days':days, 
               'hours':hours, 
               'minutes':minutes, 
               'seconds':seconds}
    
    return render(request, 'Store/index.html', context)


    # End Hot Deals: Countdown Timer view


# end view for Homepage

# View for Hot Deals


def Hotdeals(request):
    # Hot Deals: Products where new price < or 1/2 of old price
    hotdeals = AllProduct.objects.filter(new_price__lte=models.F('old_price') /2 )

    context = {'products':hotdeals}
    return render(request, 'Store/store.html', context)


# end view for Hot Deals

# view for subcategories


def Laptops(request):
    # Laptops: Products where subcategory = 'Laptops'

    laptops = AllProduct.objects.filter(subcategory='Laptops')

    # Counting total products for each subcategory

    laptops_count = AllProduct.objects.filter(subcategory='Laptops').count()
    smartphones_count = AllProduct.objects.filter(subcategory='Smartphones').count()
    cameras_count = AllProduct.objects.filter(subcategory='Cameras').count()
    accessories_count = AllProduct.objects.filter(category='Accessories').count()

    # Adding discount percentage to each product of laptops

    for products in laptops:
        if products.new_price < products.old_price:
            discount_percentage = ((products.old_price - products.new_price) / products.old_price) * 100
            products.discount_percentage = round(discount_percentage, 2) # Stores calculated discount percentage with 2 decimal places
        else:
            products.discount_percentage = "No Offers"

    context = {'products': laptops, 
               'laptopscount': laptops_count,
               'smartphonescount': smartphones_count,
               'camerascount': cameras_count,
               'accessoriescount': accessories_count}
    return render(request, 'Store/store.html', context)


def Smartphones(request):
    # Smartphones: Products where subcategory = 'Smartphones'

    smartphones = AllProduct.objects.filter(subcategory='Smartphones')

    # Counting total products for each subcategory

    laptops_count = AllProduct.objects.filter(subcategory='Laptops').count()
    smartphones_count = AllProduct.objects.filter(subcategory='Smartphones').count()
    cameras_count = AllProduct.objects.filter(subcategory='Cameras').count()
    accessories_count = AllProduct.objects.filter(category='Accessories').count()

    # Adding discount percentage to each product of laptops

    for products in smartphones:
        if products.new_price < products.old_price:
            discount_percentage = ((products.old_price - products.new_price) / products.old_price) * 100
            products.discount_percentage = round(discount_percentage, 2) # Stores calculated discount percentage with 2 decimal places
        else:
            products.discount_percentage = "No Offers"

    context = {'products': smartphones , 
               'smartphonescount': smartphones_count,
               'laptopscount': laptops_count,
               'camerascount': cameras_count,
               'accessoriescount': accessories_count,}
    return render(request, 'Store/store.html', context)


def Cameras(request):
    # Cameras: Products where subcategory = 'Cameras'

    cameras = AllProduct.objects.filter(subcategory='Cameras')

    # Counting total products for each subcategory

    laptops_count = AllProduct.objects.filter(subcategory='Laptops').count()
    smartphones_count = AllProduct.objects.filter(subcategory='Smartphones').count()
    cameras_count = AllProduct.objects.filter(subcategory='Cameras').count()
    accessories_count = AllProduct.objects.filter(category='Accessories').count()

    # Adding discount percentage to each product of laptops

    for products in cameras:
        if products.new_price < products.old_price:
            discount_percentage = ((products.old_price - products.new_price) / products.old_price) * 100
            products.discount_percentage = round(discount_percentage, 2) # Stores calculated discount percentage with 2 decimal places
        else:
            products.discount_percentage = "No Offers"

    context = {'products': cameras , 
               'camerascount': cameras_count,
               'laptopscount': laptops_count,
               'smartphonescount': smartphones_count,
               'accessoriescount': accessories_count}
    return render(request, 'Store/store.html', context)


def Accessories(request):
    # Accessories: Products where subcategory = 'Accessories'

    accessories = AllProduct.objects.filter(category='Accessories')

    # Counting total products for each subcategory

    laptopss_count = AllProduct.objects.filter(subcategory='Laptops').count()
    smartphones_count = AllProduct.objects.filter(subcategory='Smartphones').count()
    cameras_count = AllProduct.objects.filter(subcategory='Cameras').count()
    accessories_count = AllProduct.objects.filter(category='Accessories').count()

    # Adding discount percentage to each product of laptops

    for products in accessories:
        if products.new_price < products.old_price:
            discount_percentage = ((products.old_price - products.new_price) / products.old_price) * 100
            products.discount_percentage = round(discount_percentage, 2) # Stores calculated discount percentage with 2 decimal places
        else:
            products.discount_percentage = "No Offers"

    context = {'products': accessories ,
               'accessoriescount': accessories_count,
               'laptopscount': laptopss_count,
               'smartphonescount': smartphones_count,
               'camerascount': cameras_count}
    return render(request, 'Store/store.html', context)
    

# end view for subcategories

# View for Newsletter subscribtion

def Subscribe(request):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            subscriber = form.save()

            send_mail('''Subscription confirmation !
                         Thank you for subscribing our Electro Jungle Newsletter. 
                         We'll keep you updated with the latest products and offers.''', # Email body

                         settings.EMAIL_HOST_USER, # Sender email
                         [subscriber.email], # Receiver email
                         fail_silently=True, # If there is an error in sending email, it will fail silently
                    ) # Send email to the subscriber from electrojungle to Subscribers

            messages.success(request, 'You have successfully subscribed to our newsletter!') # It will show pop-up on website when user will subscribe

            return redirect('index')  # Redirect to the homepage after successful subscription
        else:
            form = SubscribersForm()

            context = {'form': form}
            return render(request, 'Store/blank.html', context)
    else:
        messages.error(request, 'Invalid form submission. Please try again.') # It will show pop-up on website when user will submit invalid form
    return redirect('index')  # Redirect to the homepage after unsuccessful subscription

# end view for Newsletter subscribstion

def Aboutus(request):
    
    # Getting Contact Info of a Company
    All_contacts = Contact_company.objects.first()  # Assuming there's only one contact info entry

    context = {'companydetails': All_contacts}
    return render(request, 'Store/blank.html', context)


# View for products search form

def Search(request):
    query = request.GET.get('query', '')
    category = request.GET.get('category', '')

    if category:
        products = AllProduct.objects.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(subcategory__icontains=query) , category__iexact=category)

    else:
        products = AllProduct.objects.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(subcategory__icontains=query))

    context = {'products': products,
               'category': category,
               'query': query,}
    
    return render(request, 'Store/store.html', context)


def Productdetails(request, pk):
    productdetail = get_object_or_404(AllProduct, pk=pk)
    related_products = AllProduct.objects.filter(subcategory=productdetail.subcategory).exclude(pk=productdetail.pk)[:4]
    context = {'productdetail': productdetail , 'related_products': related_products}
    return render(request, 'Store/product.html', context)

def Cartview(request):
    return render(request, 'Store/checkout.html')
