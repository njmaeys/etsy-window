from django.urls import path

from .views.index import index
from .views.login import login
from .views.contact import contact
from .views.get_started import get_started

urlpatterns = [
    path('', index, name='home'),
    path('login/', login, name='login'),
    path('contact/', contact, name='contact'),
    path('get-started/', get_started, name='get-started'),
]