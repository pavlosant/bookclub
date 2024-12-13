from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import generic
from .models import Book, BookClub, Meeting
from django.template import loader
# Create your views here.

class IndexView(generic.ListView):
    template_name= "bookclub/home.html"
    context_object_name= "meetings_list"

    def get_queryset(self):
        return Meeting.objects.all()

class BooksView(generic.ListView):
    template_name = "bookclub/books.html"
    context_object_name = "books_list"

    def get_queryset(self):
        books_list = Book.objects.order_by("-created_at")
        return books_list
    
class MeetingsView(generic.ListView):
    template_name = "bookclub/meetings.html"
    context_object_name = "meetings_list"

    def get_queryset(self):
        meetings_list = Meeting.objects.all()
        return meetings_list

class MeetingDetailView(generic.DetailView):
    model = Meeting
    template_name="bookclub/meeting_detail.html"
#def home(request):
#    template = loader.get_template("bookclub/home.html")
#    meetings_list = Meeting.objects.all()
#    context = {
#        "meetings_list": meetings_list
#    }
#    return HttpResponse(template.render(context, request))
    

#def meeting_detail(request, meeting_id):
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

