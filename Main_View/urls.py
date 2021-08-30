from . import views
from django.urls import path

urlpatterns = [
    path("", views.home_page),
    path('Order-Details/<int:order_id>', views.order_details_page)
]
