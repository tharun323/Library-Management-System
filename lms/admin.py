from django.contrib import admin
from lms.models import Books
from django.urls import path,include

admin.site.register(Books)

