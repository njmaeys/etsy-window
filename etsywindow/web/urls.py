from django.urls import path

from .views.index import index
from .views.login import login
from .views.contact import contact
from .views.sign_up import sign_up

urlpatterns = [
    path('', index, name='home'),
    path('login/', login, name='login'),
    path('contact/', contact, name='contact'),
    path('sign-up/', sign_up, name='sign-up'),
]