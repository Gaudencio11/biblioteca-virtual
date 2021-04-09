# biblioteca-virtual
Site em que o usuário se cadastra e armazena livros lidos, bem como suas informações

Funções específicas:
views Principais: 
Views de login; principal; adicionar livros; vizualizar livros.

Cadastrar livros atribuindo valores: Nome, autor, foto, genero, avaliação.
O livro é atrelado ao usuário
O usuário só consegue ver os própios livros

Features:
Filtro.
Baixar planilha excel com seus livros.

#Notas
Recomendo criar um superuser para acessar a página admin
(py manage.py createsuperuser)
O genero de um livro só pode ser adicionado na página de admin

database configurado para postgrees
Se não tiver postgrees instalafo pode usar o sqlite (codigo comentado em settings)

