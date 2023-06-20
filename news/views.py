from rest_framework.views import Response, Request, status, APIView
from .serializers import NewsReviewSerializer, NewsSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAdminOrReadOnly
from .models import News
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
