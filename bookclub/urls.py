from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
    path("books/", views.BooksView.as_view(), name="books_list"),
    path("books/add/", views.BookCreateView.as_view(), name="books-add"),
    path(
        "books/<int:pk>/update/",
        views.BookUpdateView.as_view(),
        name="book-update",
    ),
    path(
        "books/<int:pk>",
        views.BookDetailView.as_view(),
        name="book_detail",
    ),
    path("meetings/", views.MeetingsView.as_view(), name="meetings_list"),
    path(
        "meetings/<int:pk>",
        views.MeetingDetailView.as_view(),
        name="bookclub/meeting_detail",
    ),
    path("meetings/add/", views.MeetingCreateView.as_view(), name="meetings-add"),
    path(
        "meetings/<int:pk>/update/",
        views.MeetingUpdateView.as_view(),
        name="bookclub/meeting-update",
    ),
    path(
        "meeting/<int:pk>/delete/",
        views.MeetingDeleteView.as_view(),
        name="meeting-delete",
    ),
    # path("<int:meeting_id>/", views.meeting_detail, name="meeting_detail"),
]
