from django.urls import path
from .views import (BookView, DetailBookView, CreateBookView,
                    UpdateBookView, DeleteBookView, AuthorView, DetailAuthorView, DeleteAuthorView, UpdateAuthorView,
                    CreateAuthorView, GetBookAuthorView)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', BookView.as_view()),
    path('<int:book_id>', DetailBookView.as_view()),
    path('create/', CreateBookView.as_view()),
    path('update/<int:book_id>/', UpdateBookView.as_view()),
    path('delete/<int:book_id>/', DeleteBookView.as_view()),
    path('author', AuthorView.as_view()),
    path('author/<int:author_id>', DetailAuthorView.as_view()),
    path('author/create/', CreateAuthorView.as_view()),
    path('author/update/<int:author_id>/', UpdateAuthorView.as_view()),
    path('author/delete/<int:author_id>/', DeleteAuthorView.as_view()),
    path('author_books/<int:author_id>', GetBookAuthorView.as_view())
]
