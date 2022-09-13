from django.urls import path

from . import views

urlpatterns = [
    path("item/<int:item_id>/", views.get_item_view, name="item-view"),
    path("buy/<int:item_id>", views.create_stripe_session, name="stripe-session"),
]
