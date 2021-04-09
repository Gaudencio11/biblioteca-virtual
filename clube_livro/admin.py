from django.contrib import admin
from .models import Livro, Genero
from django.conf.urls import url
from .views import excel_books

admin.site.register(Livro)
admin.site.register(Genero)




