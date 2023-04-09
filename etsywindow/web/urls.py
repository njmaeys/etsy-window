from django.urls import path

from .views.index import index
from .views.login import login_view
from .views.contact import contact
from .views.sign_up import sign_up
from .views.portal import portal_home
from .views.logout import logout_view

urlpatterns = [
    path('', index, name='home'),
    path('login/', login_view, name='login'),
    path('contact/', contact, name='contact'),
    path('sign-up/', sign_up, name='sign-up'),
    path('portal-home/', portal_home, name='portal-home'),
    path('logout/', logout_view, name='logout'),
]