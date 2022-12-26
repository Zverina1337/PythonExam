from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView
from .models import Product
from .forms import ProductForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

class index(TemplateView):
    template_name = 'index.html'

class about(TemplateView):
    template_name = 'about.html'

class contacts(TemplateView):
    template_name = 'contacts.html'
    
class services(ListView):
    model = Product
    template_name = 'services_list.html'
    context_object_name = 'services'

class CreateProduct(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    login_url = '/login'
    success_url = '/services'
    template_name = 'add_product.html'

class login(LoginView):
    model = User
    template_name = 'login.html'