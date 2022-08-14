from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, DonatePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('donate/', DonatePageView.as_view(), name='donate'),
]