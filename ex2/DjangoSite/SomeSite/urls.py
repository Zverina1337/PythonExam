from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index.as_view(), name='home'),
    path('about', about.as_view(), name='about'),
    path('contacts', contacts.as_view(), name='contacts'),
    path('services', services.as_view(), name='services'),
    path('login', login.as_view(), name='login'),
    path('create', CreateProduct.as_view(), name='create_product')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)