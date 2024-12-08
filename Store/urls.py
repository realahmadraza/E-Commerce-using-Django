from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.Index, name='index'),
    path('search/', views.Search, name='search'),
    path('laptops/', views.Laptops, name='laptops'),
    path('smartphones/', views.Smartphones, name='smartphones'),
    path('cameras/', views.Cameras, name='cameras'),
    path('accessories/', views.Accessories, name='accessories'),
    path('hotdeals/', views.Hotdeals, name='hotdeals'),
    path('subscribe us/', views.Subscribe, name='subscribe'),
    path('blank/', views.Aboutus, name='aboutus'),
    path('product/<int:pk>/', views.Productdetails, name='productdetails'),
    path('my cart/', views.Cartview, name='cartview'),
    #path('saving/<int:pk>/', views.Addtocart, name='addtocart'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)