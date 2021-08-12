from users.models import User
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from blogpost.utils import create_id
from .authentication import is_authorized, validate_password, generate_token, hash_password
from .serializers import UserCreationRequestRequestSerializer

class UserView(APIView):

    def post(self, request):

        user_data = JSONParser().parse(request)
        serializer = UserCreationRequestRequestSerializer(data=user_data)   
        user = serializer.create_user()

        if not user.has_valid_display_name():
            return JsonResponse({'message' : user.notification}, status=status.HTTP_400_BAD_REQUEST)

        if not user.has_valid_email():
            return JsonResponse({'message' : user.notification}, status=status.HTTP_400_BAD_REQUEST)

        if not user.has_valid_password():
            return JsonResponse({'message' : user.notification}, status=status.HTTP_400_BAD_REQUEST)

        if user.has_existing_email():
            return JsonResponse({'message' : user.notification}, status=status.HTTP_409_CONFLICT)

        user.id = create_id("usr")
        user.password = hash_password(user.password)
        user.save()

        return JsonResponse({'token' : generate_token(user)}, status=status.HTTP_201_CREATED)



class LoginView(APIView):

    def post(self, request):

        login_data = JSONParser().parse(request)
        
        if "email" not in login_data:
            return JsonResponse({'message' : '"email" is required'}, status=status.HTTP_400_BAD_REQUEST)

        if not login_data["email"]:
            return JsonResponse({'message' : '"email" is not allowed to be empty'}, status=status.HTTP_400_BAD_REQUEST)
        
        if "password" not in login_data:
            return JsonResponse({'message' : '"password" is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not login_data["password"]:
            return JsonResponse({'message' : '"password" is not allowed to be empty'}, status=status.HTTP_400_BAD_REQUEST)
            

        user = User.objects.filter(email=login_data["email"])

        if not user or not validate_password(login_data["password"], user.first().password):
            return JsonResponse({'message' : 'Campos inválidos'}, status=status.HTTP_400_BAD_REQUEST)
         
        return JsonResponse({'token' : generate_token(user.first())}, status=status.HTTP_200_OK)


        