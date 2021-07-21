from django.urls import path
from .views import List, Upload, Myimages, Delete

urlpatterns = [
     path('list', List.as_view()),
     path('upload', Upload.as_view()),
     path('myimages', Myimages.as_view()),
     path('delete', Delete.as_view()),

]