from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

class CustomLoginView(ObtainAuthToken):

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        data = {}

        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            data = {
                'token': token.key,
                'username': user.username,
                'user_id': user.id
            }
            resp_status = status.HTTP_200_OK
        else:
            data = serializer.errors
            resp_status = status.HTTP_400_BAD_REQUEST
        return Response(data, status=resp_status)
