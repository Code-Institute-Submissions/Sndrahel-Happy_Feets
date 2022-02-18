from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(verbose_name=_('Name'), max_length=254)
    friendly_name = models.CharField(
        max_length=254, blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(
        max_length=250, blank=True)
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        verbose_name=_('Rating'),
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(
        max_length=2000, blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return f'{self.name}'


class Review(models.Model):

    class Meta:
        ordering = ['id']

    user = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_review = models.TextField(
        verbose_name=_('User Review'), max_length=250, null=False, blank=False)
    product_rating = models.IntegerField(
        choices=[(5, '5'), (4, '4'), (3, '3'), (2, '2'), (1, '1'), ],
        default=5)
    title = models.CharField(
        verbose_name=_('Review Title'), max_length=25, null=False, blank=False)
    user_review = models.TextField(
        verbose_name=_('User Review'), max_length=250, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
