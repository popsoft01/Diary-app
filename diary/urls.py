
from django.urls import path

from . import views

urlpatterns = [
    path("", views.EntryListView.as_view(), name="entry-list"),
    path(
        "diary/<int:pk>", views.EntryDetailView.as_view(), name="entry-detail"
    ),
    path("create", views.EntryCreateView.as_view(), name="entry-create"),
    path(
        "diary/<int:pk>/update",
        views.EntryUpdateView.as_view(),
        name="entry-update",
    ),
    path(
        "diary/<int:pk>/delete",
        views.EntryDeleteView.as_view(),
        name="entry-delete",
    ),
]
