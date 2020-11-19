from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('books/', views.BookListView.as_view(), name='books'),
   path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
   path('authors/', views.AuthorListView.as_view(), name='authors'),
   path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
   path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='prestados'),
   path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
   path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
   # path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
   # path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]

# Sample: from cofeeHouse
# from .views import (main_page,
#                    contact_page,
#                    about_page)

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('contact/', contact_page),
#     path('about/', about_page),
#     path('', main_page),
# ]