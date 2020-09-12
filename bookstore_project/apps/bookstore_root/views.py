from django.shortcuts import render
from bookstore_project.apps.products.models import Book

# Create your views here.
def index(request):
	books = Book.objects.all()
	return render(request, 'bookstore_root/index.html',{'books':books})