from django.urls import path
from .views import profileView, readView, addView, deleteView, updateView, \
    authView, detailView, wish_list, add_wish_list, mainView, excel_books
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', mainView, name='main'),
    path('profile/', profileView, name = 'profile'),
    path('read/', readView, name='read' ),
    path('add/', addView, name = 'add'),
    path('delete/<int:id>/', deleteView, name= 'delete'),
    path('update/<int:id>/', updateView, name='update'),
    path('detail/<int:id>/', detailView, name='detail'),
    path('auth/', authView, name='author'),
    path('list/', wish_list, name='wish'),
    path('add_wish/', add_wish_list, name='add_wish' ),
    path('export_excel/', excel_books, name='export_excel' )

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)