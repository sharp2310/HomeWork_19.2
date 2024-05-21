from django.urls import path

from catalog.apps import MainappConfig
from catalog.views import home, contact, products_list,  create

app_name = MainappConfig.name
urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contact, name='contact'),
    path('product/<int:pk>', products_list, name='product'),
    path('create/', create, name='create'),
]