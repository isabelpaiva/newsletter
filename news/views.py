from rest_framework.views import Response, Request, status, APIView
from .serializers import NewsReviewSerializer, NewsSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAdminOrReadOnly, IsReviewerOwner
from .models import News, NewsReview
from django.shortcuts import get_object_or_404

class CreateListNewView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    def post(self, request: Request):
        serializer = NewsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)
    

class CreateListReview(APIView):
    authentication_classes = [JWTAuthentication]
    def post(self, request: Request, news_id: int):
        serializer = NewsReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        news = get_object_or_404(News, id=news_id)
        serializer.save(news=news, reviewer=request.user)
        return Response(serializer.data, status.HTTP_201_CREATED)


class DeleteReview(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsReviewerOwner]
    def delete(self, request, news_id: int, review_id: int):
        review = get_object_or_404(NewsReview, id=review_id)
        self.check_object_permissions(request, review)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)