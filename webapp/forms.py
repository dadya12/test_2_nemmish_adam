from django import forms
from webapp.models import Product, Review

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'image']

class ReviewForm(forms.ModelForm):
    class Meta:
        model =Review
        fields = ['author', 'product', 'text', 'rating', 'moderate']


class ProductUserForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['users']
        widgets = {'users': forms.CheckboxSelectMultiple}