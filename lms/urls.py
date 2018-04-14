from django.urls import path,include
from . import views
from . import models
app_name='lms'
urlpatterns=[
    path('',views.home,name='home'),
    path('<int:book_id>/',views.claim,name='claim'),

]
