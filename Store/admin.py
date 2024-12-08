from django.contrib import admin
from .models import AllProduct, Contact_company, Subscribers, Hotdealscountdown, Cart, Cartitem


# Register your models here.


@admin.register(AllProduct)

class Product_Admin(admin.ModelAdmin):
    list_display = ('title' , 'image' , 'video' , 'description' , 'old_price' , 'new_price' , 'category' , 'subcategory' , 'sales' , 'created_at' , 'updated_at')

    search_fields = ('title', 'category', 'subcategory', 'sales', 'old_price', 'new_price')

    list_filter = ('title', 'category', 'subcategory', 'sales', 'old_price', 'new_price')

@admin.register(Cart)

class Cart_Admin(admin.ModelAdmin):
    list_display = ('user' , 'created_at')
    search_fields = ('user', 'created_at')
    list_filter = ('user',)

@admin.register(Cartitem)

class Cartitem_Admin(admin.ModelAdmin):
    list_display = ('user' , 'product' , 'quantity')
    search_fields = ('user',)
    list_filter = ('user',)


admin.site.register(Hotdealscountdown)


@admin.register(Contact_company)

class Contact_Info_Admin(admin.ModelAdmin):
    list_display = ('company_name' , 'phone' , 'email', 'about_us')


@admin.register(Subscribers)

class Subscribers_Admin(admin.ModelAdmin):
    list_display = ('email' , 'subscribed_at')