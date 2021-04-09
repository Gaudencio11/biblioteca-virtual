from django.forms import ModelForm
from .models import Livro, WishList

class RegistrarLivro(ModelForm):
    class Meta:
        model = Livro
        fields = ['id','book_title','book_author', 'book_image',
                  'book_publisher','book_type',
                  'book_sinopse',
                  'user_experience','user_rating']

class RegistraLista(ModelForm):
    class Meta:
        model = WishList
        fields = ['book_name']