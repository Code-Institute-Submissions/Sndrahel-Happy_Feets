from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_treatments, name='treatments'),
    path('<package_id>', views.package_detail, name='package_detail'),
]