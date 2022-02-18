"""
Code for reviews where adapted from:
https://github.com/johnvenkiah/CI_PP5_John_Venkiah
"""

from django import forms
from django.forms import Textarea, Select, ModelForm
from .widgets import CustomClearableFileInput
from .models import Product, Category, Review


class ReviewForm(ModelForm):

    class Meta:
        model = Review
        fields = ('title', 'product_rating', 'user_review',)

        widgets = {'product_rating': Select(
            attrs={'id': 'product_rating', 'class': 'custom-select'}),
            'user_review': Textarea(attrs={'rows': 5}), }


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        categories = Category.objects.all()  # pylint: disable=no-member
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
