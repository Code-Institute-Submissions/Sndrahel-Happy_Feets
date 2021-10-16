from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

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
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(
        max_length=2000, blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name

# Add Rating to Product Description. Code adapted from: https://amethyst-lynx-91ku816p.ws-eu17.gitpod.io/
    def get_rating(self):
        total = sum(int(review['stars']) for review in self.reviews.values())

        if self.reviews.count() > 0:
            return total / self.reviews.count()
        else:
            return 0


# Product Review. Code adapted from: https://amethyst-lynx-91ku816p.ws-eu17.gitpod.io/
class ProductReview(models.Model):
    product = models.ForeignKey(
        Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name="reviews", on_delete=models.CASCADE
    )

    content = models.TextField(blank=True)
    stars = models.IntegerField()

    date_added = models.DateTimeField(auto_now_add=True)
