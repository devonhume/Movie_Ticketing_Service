from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('showings/<int:movie_id>/', views.showings_view, name='showings'),
    path('purchase/<int:showing_id>', views.purchase_view, name='purchase'),
]