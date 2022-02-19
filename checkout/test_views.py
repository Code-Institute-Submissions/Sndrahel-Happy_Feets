from django.test import TestCase
from django.contrib.auth.models import User

from checkout.models import Order
from profiles.models import UserProfile


class TestCheckoutViews(TestCase):

    def setUp(self):
        test_user = User.objects.create_user(
            username='test_user', password='test_password')
        test_user_superuser = User.objects.create_superuser(
            username='test_user_superuser', password='test_password')

        test_user.save()
        test_user_superuser.save()
        test_user = UserProfile.objects.get(user=test_user)

        Order.objects.create(
            full_name='Test User',
            email='test_email@mail.com',
            phone_number='123456789',
            town_or_city='Test City',
            street_address1='Test Street 2',
            user_profile=test_user
        )

    def tearDown(self):
        Order.objects.all().delete()
