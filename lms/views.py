from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
import datetime
from django.shortcuts import get_list_or_404
from . models import Books
def home(request):
    book_list=Books.objects.all()
    context={
        'book_list':book_list
    }
    query=request.GET.get("q")
    if query:
        book_list=book_list.filter(book_name__icontains=query)
        return render(request, 'lms/home.html', context)
    return render(request, 'lms/home.html', context)


def claim(request,book_id):
    book=Books.objects.get(pk=book_id)
    context={
        'book':book
    }
    return render(request,'lms/claim.html',context)
