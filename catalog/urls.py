from django.urls import path

from catalog.views import home, contact, product, create
from catalog.apps import MainappConfig

app_name = MainappConfig.name
urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contact, name='contact'),
    path('product/<int:pk>', product, name='product'),
    path('create/', create, name='create'),
]