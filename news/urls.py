from django.urls import path
from .views import CreateListNewView, CreateListReview, DeleteReview, UpdateNewsView

urlpatterns = [
    path('news/', CreateListNewView.as_view()),
    path('news/<int:news_id>/review/', CreateListReview.as_view()),
    path('news/<int:news_id>/review/<int:review_id>/', DeleteReview.as_view()),
    path('news/<int:news_id>/', UpdateNewsView.as_view()),
]