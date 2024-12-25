from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import generic
from .models import Book, BookClub, Meeting
from django.template import loader
import datetime
from django.urls import reverse_lazy
from django.contrib.admin.widgets import AdminDateWidget

# Create your views here.


class IndexView(generic.ListView):
    template_name = "bookclub/home.html"
    context_object_name = "meetings_list"
    queryset = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_meetings = Meeting.objects.order_by("-meeting_date")
        all_meetings_asc = Meeting.objects.order_by("meeting_date")
        future_meetings = [
            meeting for meeting in all_meetings_asc if meeting.meeting_in_the_future
        ]
        context["next_meeting"] = future_meetings[0] if future_meetings else None
        return context


class BooksView(generic.ListView):
    template_name = "bookclub/books.html"
    context_object_name = "books_list"

    def get_queryset(self):
        books_list = Book.objects.order_by("-created_at")
        non_discussed_books = Book.objects.filter(discussed=False).order_by(
            "title", "author"
        )
        discussed_books = Book.objects.filter(discussed=True).order_by(
            "title", "author"
        )

        queryset = {
            "non_discussed_books": non_discussed_books,
            "discussed_books": discussed_books,
        }
        return queryset


class BookCreateView(generic.CreateView):
    model = Book
    fields = "__all__"


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = "__all__"


class BookDeleteView(generic.DeleteView):
    model = Book
    success_url = reverse_lazy("books_list")


class BookDetailView(generic.DetailView):
    model = Book
    template_name = "bookclub/book_detail.html"


class MeetingsView(generic.ListView):
    template_name = "bookclub/meetings.html"
    context_object_name = "meetings_list"

    def get_queryset(self):
        future_meetings = []
        past_meetings = []
        all_books = Meeting.objects.order_by("meeting_date")

        for book in all_books:
            if book.meeting_in_the_future == True:
                future_meetings.append(book)

            else:
                past_meetings.insert(0, book)

        queryset = {
            "all_meetings": Meeting.objects.order_by("meeting_date"),
            "future_meetings": future_meetings,
            "past_meetings": past_meetings,
            "next_meeting:": future_meetings[0] if future_meetings else None,
        }
        # meetings_list = Meeting.objects.order_by("-meeting_date")
        return queryset


class MeetingDetailView(generic.DetailView):
    model = Meeting
    template_name = "bookclub/meeting_detail.html"

    def get_form(self, form_class=None):
        form = super(MeetingDetailView, self).get_form(form_class)
        form.fields["meeting_date"].widget = AdminDateWidget(attrs={"type": "date"})
        return form


class MeetingCreateView(generic.CreateView):
    model = Meeting
    fields = "__all__"

    def get_form(self, form_class=None):
        form = super(MeetingCreateView, self).get_form(form_class)
        form.fields["meeting_date"].widget = AdminDateWidget(attrs={"type": "date"})
        return form


class MeetingUpdateView(generic.UpdateView):
    model = Meeting
    fields = "__all__"

    def get_form(self, form_class=None):
        form = super(MeetingUpdateView, self).get_form(form_class)
        form.fields["meeting_date"].widget = AdminDateWidget(attrs={"type": "date"})
        return form


class MeetingDeleteView(generic.DeleteView):
    model = Meeting
    success_url = reverse_lazy("meetings_list")

    def get_form(self, form_class=None):
        form = super(MeetingDeleteView, self).get_form(form_class)
        form.fields["meeting_date"].widget = AdminDateWidget(attrs={"type": "date"})
        return form


class ProfileView(generic.TemplateView):
    template_name = "account/profile.html"


# def home(request):
#    template = loader.get_template("bookclub/home.html")
#    meetings_list = Meeting.objects.all()
#    context = {
#        "meetings_list": meetings_list
#    }
#    return HttpResponse(template.render(context, request))


# def meeting_detail(request, meeting_id):
#    meeting = get_object_or_404(Meeting, pk=meeting_id)
#    return render(request, "bookclub/meeting_detail.html", {"meeting":meeting})

# def books_list(request):
#     books_list = Book.objects.order_by("-created_at")
#     template = loader.get_template("bookclub/books.html")
#     context = {
#         "books_list": books_list
#     }
#     return HttpResponse(template.render(context, request))

# def meetings_list(request):
#     meetings_list = Meeting.objects.all()
#     template = loader.get_template("bookclub/meetings.html")
#     context = {
#         "meetings_list": meetings_list
#     }
#     return HttpResponse(template.render(context, request))
