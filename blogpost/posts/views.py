from django.utils import timezone
from blogpost.utils import create_id
from rest_framework import status
from rest_framework.parsers import JSONParser
from posts.models import Post
from rest_framework.views import APIView
from users.authentication import is_authorized, get_user
from django.http.response import HttpResponse, JsonResponse
from .serializers import PostCreationRequestSerializer, PostCreationResponseSerializer, PostSearchRequestSerializer

SEARCH_PARAM = 'q'

class PostView(APIView):

    @is_authorized()
    def post(self, request):
        
        user_data = JSONParser().parse(request)
        serializer = PostCreationRequestSerializer(data=user_data)
        post_object = serializer.create_post()

        if not post_object.has_valid_title():
            return JsonResponse({'message': post_object.notification}, status=status.HTTP_400_BAD_REQUEST)

        if not post_object.has_valid_content():
            return JsonResponse({'message': post_object.notification}, status=status.HTTP_400_BAD_REQUEST)

        post_object.id = create_id("usr")
        post_object.user = get_user(request)
        post_object.published = timezone.localtime()
        post_object.save()

        return JsonResponse(PostCreationResponseSerializer(post_object, many=False).data, status=status.HTTP_201_CREATED)

    @is_authorized()   
    def get(self, request):
        posts = Post.objects.all()
        post_serializer = PostSearchRequestSerializer(posts, many=True)
        return JsonResponse(post_serializer.data, safe=False)


class PostDetailsView(APIView):

    @is_authorized()
    def put(self, request, id):
        pass

    @is_authorized()    
    def get(self, request, id):
        pass

    @is_authorized()    
    def delete(self, request, id):
        pass

class PostSearchView(APIView):
    
    @is_authorized()
    def get(self, request):
        print(request.query_params.get(SEARCH_PARAM))