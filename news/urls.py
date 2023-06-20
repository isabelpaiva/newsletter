from django.urls import path
from .views import CreateListNewView, CreateListReview

urlpatterns = [
    path('news/', CreateListNewView.as_view()),
    path('news/<int:news_id>/review/', CreateListReview.as_view()),
    # path('news/<int:news_id>/review/<int:review_id>/', DeleteReview.as_view()),

]