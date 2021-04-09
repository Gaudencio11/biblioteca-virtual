from django.db import models
from django.contrib.auth.models import User

RATING_USER = [
    ('0','0'),
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
]

#Genreo dos livros. Só pode ser adicionado e deitado pelo adm da página
class Genero(models.Model):
    type = models.CharField(max_length=100, verbose_name='Generos:')

    def __str__(self):
        return self.type


class Livro(models.Model):
    book_title = models.CharField(max_length=200, verbose_name='Título do '
                                                               'Livro:')

    book_author = models.CharField(max_length=200, verbose_name='Autor:',
                                   blank=True)
    book_image = models.FileField( upload_to="media/images/", null=True,
                                   blank=True)
    book_publisher = models.CharField(max_length=200,
                                      verbose_name='Editora:', null=True, blank=True)
    book_type = models.ForeignKey(Genero, related_name='Genero', null=True,
                                 blank=True, on_delete=models.SET_NULL,
                                  verbose_name='Gênero do Livro:')

    book_sinopse = models.TextField(verbose_name='Sinopse:', null=True, blank=True)
    #autor da estante de livros, Tirar depois a opção null e blank
    auth = models.ForeignKey(User, on_delete=models.CASCADE, blank=True )
    user_experience = models.TextField(verbose_name='Como foi ler esse '
                                                    'livro:', null=True, blank=True)
    user_rating = models.CharField(max_length=20, choices=RATING_USER,
                                   default='0',verbose_name='Avaliação')

    def __str__(self):
        return self.book_title

class WishList(models.Model):
    list_auth = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    book_name = models.CharField(max_length=100, verbose_name='Título do '
                                                               'Livro:')










