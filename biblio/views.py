from django.shortcuts import render
from django.views import View
from .models import Book

# Create your views here.


class IndexView(View):
    def get(self, request):
        return render(request, 'biblio/index.html')


class BookView(View):
    def get(self, request):
        context = {'book_obj': Book.objects.all()}
        return render(request, 'biblio/book_list.html', context)