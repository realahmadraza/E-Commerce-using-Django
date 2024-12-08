from typing import Any
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Create your models here.


class AllProduct(models.Model):
    title = models.CharField(max_length=255)
    explained_title = models.CharField(max_length=255 , default='no detail provided by seller')
    image = models.ImageField(upload_to='products/images/')
    video = models.FileField(upload_to='products/videos/', blank=True, null=True)
    description = models.TextField()
    Details = models.TextField(null=True, default='No Details provided by seller')
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)
    sales = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=(('Not orderd', 'Not Ordered'),('Pending', 'Pending'), ('Ready for ship', 'Ready for ship'), ('Order shipped', 'Order shipped'), ('Out of delivery', 'Out of delivery'), ('Delivered', 'Delivered')), default='')


    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Cart for {self.user}'
    
class Cartitem(models.Model):
    user = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(AllProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self) -> str:
        return f'{self.quantity} of {self.product}'


class Hotdealscountdown(models.Model):
    title = models.CharField(max_length=100, default='HOT DEALS THIS WEEK')
    description = models.TextField(default='NEW COLLECTION UP TO 50% OFF')
    end_date_time = models.DateTimeField()  # The end date and time for the countdown

    def __str__(self):
        return f'Hot deals countdown {self.title}'


class Subscribers(models.Model):
    email = models.EmailField(max_length=100, blank=False)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Subscribers | {self.email}  |  {self.subscribed_at}'


class Contact_company(models.Model):
    company_name = models.CharField(max_length=20, blank=False)
    phone = PhoneNumberField(region='US')
    email = models.EmailField(max_length=100, blank=False)
    aboutus_main = models.CharField(default='Our networks and offices are available throught the whole world.', max_length=100, blank=False)
    about_us = models.TextField(default='' ,blank=False)
    privacy_policy = models.TextField(default='', blank=False)
    Terms_and_conditions = models.TextField(default='', blank=False)

    def __str__(self):
        return f'ContactInfo | {self.company_name}   |    {self.phone}  |   {self.email}   |   {self.aboutus_main}' 
    

