from django.urls import path

from .views import HomePageView, AttackPageView, DefencePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('attack/<pk>/', AttackPageView.as_view(), name='attack'),
    path('defence/<pk>/', DefencePageView.as_view(), name='defence'),
]
