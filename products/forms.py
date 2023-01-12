from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.FloatField()
    size = forms.FloatField(required=False)
    stock = forms.BooleanField(required=False)
    