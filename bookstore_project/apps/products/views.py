from django.shortcuts import render
from .models import Book
from django.db.models import Q
from .forms import SearchBookBasicForm,SearchBookComplexForm

# Create your views here.
def search_book_basic(request):
	if request.GET.get('string_search'):
		form = SearchBookBasicForm(request.POST or None)
		string_search = request.GET.get('string_search','')
		books = Book.objects.filter(Q(title__icontains=string_search) | Q(author__name__icontains=string_search))
		return render(request, 'products/searchProduct.html',{'form': form, 'books':books})
	else:
		form = SearchBookBasicForm()
		return render(request, 'products/searchProduct.html',{'form': form})

def search_book_complex(request):
	if request.GET.get('string_search_author'):
		form = SearchBookComplexForm(request.POST or None)
		string_search_author = request.GET.get('string_search_author','')
		string_search_title = request.GET.get('string_search_title','')
		string_search_isbn = request.GET.get('string_search_isbn','')
		books = Book.objects.filter(Q(title=string_search_title) | Q(author__name=string_search_author) | Q(isbn=string_search_isbn))
		return render(request, 'products/searchProduct.html',{'form': form, 'books':books})
	else:
		form = SearchBookComplexForm()
		return render(request, 'products/searchProduct.html',{'form': form})


def change_class_for_error(form):
	for field in form:
		if field.errors:
			form.fields[field.name].widget.attrs['class'] = 'form-control is-invalid'