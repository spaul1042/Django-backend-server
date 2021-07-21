from django.urls import path
from. views import Test, Register, Login, UserView, Update

urlpatterns = [
    path('', Test.as_view() ),
    path('register', Register.as_view()),
    path('login', Login.as_view()),
    path('detail', UserView.as_view()),
    path('update', Update.as_view()),


]