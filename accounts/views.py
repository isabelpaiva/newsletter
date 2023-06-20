from rest_framework.views import Response, Request, status, APIView
from .serializers import AccountSerializer

class CreateListAccountView(APIView):
    def post(self, request: Request) -> Response:
        serializer = AccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)