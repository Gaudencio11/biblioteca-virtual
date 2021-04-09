import django_filters
from .models import Livro

class LivrosFilter(django_filters.FilterSet):
    class Meta:
        model = Livro
        fields = ['book_type', 'book_title']

