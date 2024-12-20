from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Book, Meeting
from django.urls import reverse
from datetime import datetime, timedelta

# Create your tests here.


class BookClubViewsTests(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(username="user1")
        self.user2 = User.objects.create(username="user2")
        self.book1 = Book.objects.create(
            title="Book 1",
            author="Author 1",
            created_at=datetime.now(),
            discussed=False,
        )
        self.book2 = Book.objects.create(
            title="Book 2",
            author="Author 2",
            created_at=datetime.now(),
            discussed=True,
        )

        self.future_meeting = Meeting.objects.create(
            meeting_date=datetime.now() + timedelta(days=10),
            location="City 1",
            host=self.user1,
        )
        self.past_meeting = Meeting.objects.create(
            meeting_date=datetime.now() - timedelta(days=10),
            location="City 2",
            host=self.user2,
        )

        self.client = Client()

    def test_home_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bookclub/home.html")
        self.assertContains(response, "Saffron Walden")

    def test_book_view(self):
        response = self.client.get(reverse("books_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bookclub/books.html")
        self.assertContains(response, "Book 1")
        self.assertContains(response, "Book 2")
        self.assertEqual(
            response.context["books_list"]["non_discussed_books"].count(), 1
        )
        self.assertEqual(response.context["books_list"]["discussed_books"].count(), 1)

    def test_meeting_view(self):
        response = self.client.get(reverse("meetings_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bookclub/meetings.html")
        self.assertContains(response, "City 1")
        self.assertEqual(len(response.context["meetings_list"]["future_meetings"]), 1)
        self.assertEqual(len(response.context["meetings_list"]["past_meetings"]), 1)

    def test_meeting_detail_view(self):
        response = self.client.get(
            reverse("bookclub/meeting_detail", args=[self.future_meeting.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "City 1")
        self.assertTemplateUsed(response, "bookclub/meeting_detail.html")

    def test_book_create_view(self):
        response = self.client.post(
            reverse("books-add"),
            {
                "title": "New book",
                "author": "New Author",
            },
        )
        self.assertEqual(response.status_code, 302)  # redirect after success
        self.assertTrue(Book.objects.filter(title="New book").exists)

    def test_book_update_view(self):
        response = self.client.put(
            reverse("book-update", args=[self.book1.id]),
            {
                "title": "Updated Book 1 title",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book 1 title")
