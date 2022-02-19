from django.test import TestCase
from shop.models import Product
from .models import Order


class TestCheckoutModels(TestCase):

    def setUp(self):
        Product.objects.create(
            sku='999',
            name='Test Name',
            price='99.99',
            description='Test Description',
        )

        Order.objects.create(
            full_name='Test Name',
            email='test@mail.com',
            phone_number='123456789',
            street_address1='Test Street',
            town_or_city='Test city',
        )

    def tearDown(self):
        Product.objects.all().delete()
        Order.objects.all().delete()

    def test_order_str_method(self):
        order = Order.objects.get(email='test@mail.com')
        self.assertEqual(str(order), order.order_number)
