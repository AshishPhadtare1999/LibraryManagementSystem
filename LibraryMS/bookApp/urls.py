from unicodedata import name
from django.urls import path
from .views import *
urlpatterns = [
    path('login/',login_view,name="login"),
    path('register/',register,name="Register"),
    path('book/',book_view,name="Book"),
    path('update/<int:id>',update_book,name="update"),
    path('delete/<int:id>',delete_book,name="delete")
]