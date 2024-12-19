from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

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
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(template_name="account/login.html"),
        name="login",
    ),
    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view(template_name="account/logout.html"),
        name="logout",
    ),
    path(
        "accounts/", include("django.contrib.auth.urls")
    ),  # Include built-in auth views
    path(
        "accounts/profile/", login_required(views.ProfileView.as_view()), name="profile"
    ),
    path(
        "accounts/password_change/",
        auth_views.PasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "accounts/password_change_done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path(
        "accounts/password_reset/",
        auth_views.PasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "accounts/password_reset_done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "accounts/reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "accounts/reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
