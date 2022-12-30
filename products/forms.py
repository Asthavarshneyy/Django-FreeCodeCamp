from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
  class Meta:
    model=Product
    fields=[
      'title',
      'description',
      'price',
    ]
  def clean_title(self, *args, **kwargs):
    title=self.cleaned_data.get('title')
    if not "CFE" in title:
      raise forms.ValidationError("This is not valid")
    return title

class RawProductForm(forms.Form):
  title= forms.CharField()
  description=forms.CharField(widget=forms.Textarea)
  price=forms.DecimalField()
  