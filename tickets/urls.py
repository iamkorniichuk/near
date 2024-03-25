from django.urls import path

from .views import TicketListView, TicketDetailsView


app_name = "tickets"

urlpatterns = [
    path("", TicketListView.as_view(), name="list"),
    path("<int:pk>/", TicketDetailsView.as_view(), name=""),
]
