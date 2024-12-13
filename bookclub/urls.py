from django.urls import path
from .import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
    path("books/", views.BooksView.as_view(), name="books_list"),
    path("meetings/", views.MeetingsView.as_view(), name="meetings_list"),
    path("meetings/<int:pk>",views.MeetingDetailView.as_view(),name="meeting_detail"),
    #path("<int:meeting_id>/", views.meeting_detail, name="meeting_detail"),
   
]
