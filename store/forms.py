from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product_name', 'lens', 'customer', 'address', 'phone', 'status']
