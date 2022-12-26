from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = Product