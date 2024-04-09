from __future__ import annotations

from apps.posts.models import Post
from apps.users.authentication import get_user
from apps.users.authentication import is_authorized
from django.db.models.query_utils import Q
from django.http.response import HttpResponse
from django.http.response import JsonResponse
from django.utils import timezone
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from utils import create_id

from .serializers import PostCreationRequestSerializer
from .serializers import PostCreationResponseSerializer
from .serializers import PostSearchRequestSerializer
from .serializers import PostUpdateResponseSerializer

SEARCH_PARAM = 'q'


class PostView(APIView):

    @is_authorized()
    def post(self, request):

        post_data = JSONParser().parse(request)
        serializer = PostCreationRequestSerializer(data=post_data)
        post_object = serializer.create_post()

        if not post_object.has_valid_title():
            return JsonResponse(
                {'message': post_object.notification},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not post_object.has_valid_content():
            return JsonResponse(
                {'message': post_object.notification},
                status=status.HTTP_400_BAD_REQUEST,
            )

        time = timezone.localtime()

        post_object.id = create_id('post')
        post_object.user = get_user(request)
        post_object.published = time
        post_object.updated = time
        post_object.save()

        return JsonResponse(
            PostCreationResponseSerializer(post_object, many=False).data,
            status=status.HTTP_201_CREATED,
        )

    @is_authorized()
    def get(self, request):
        posts = Post.objects.all()
        post_serializer = PostSearchRequestSerializer(posts, many=True)
        return JsonResponse(post_serializer.data, safe=False)


class PostDetailsView(APIView):

    @is_authorized()
    def put(self, request, id):
        post = self.get_post_by_id(id)
        user = get_user(request)

        if post is None:
            return JsonResponse({'message': 'Post não existe'}, status=status.HTTP_404_NOT_FOUND)

        if post.user_id != user.id:
            return JsonResponse({'message': 'Usuário não autorizado'}, status=status.HTTP_401_UNAUTHORIZED)

        post_data = JSONParser().parse(request)
        serializer = PostCreationRequestSerializer(data=post_data)
        post_object = serializer.create_post()

        if not post_object.has_valid_title():
            return JsonResponse({'message': post_object.notification}, status=status.HTTP_400_BAD_REQUEST)

        if not post_object.has_valid_content():
            return JsonResponse({'message': post_object.notification}, status=status.HTTP_400_BAD_REQUEST)

        post.title = post_object.title
        post.content = post_object.content
        post.updated = timezone.now()
        post.save()

        post_serializer = PostUpdateResponseSerializer(post, many=False)
        return JsonResponse(post_serializer.data, status=status.HTTP_200_OK)

    @is_authorized()
    def get(self, request, id):
        post = self.get_post_by_id(id)

        if post is None:
            return JsonResponse({'message': 'Post não existe'}, status=status.HTTP_404_NOT_FOUND)

        post_serializer = PostSearchRequestSerializer(post, many=False)
        return JsonResponse(post_serializer.data, safe=False)

    @is_authorized()
    def delete(self, request, id):
        post = self.get_post_by_id(id)
        user = get_user(request)

        if post is None:
            return JsonResponse({'message': 'Post não existe'}, status=status.HTTP_404_NOT_FOUND)

        if post.user_id != user.id:
            return JsonResponse({'message': 'Usuário não autorizado'}, status=status.HTTP_401_UNAUTHORIZED)

        post.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    def get_post_by_id(self, id):
        try:
            return Post.objects.get(pk=id)
        except Post.DoesNotExist:
            return None


class PostSearchView(APIView):

    @is_authorized()
    def get(self, request):
        query = request.query_params.get(SEARCH_PARAM)

        if query is None or not query:
            posts = Post.objects.all()
        else:
            title_filter = Q(title__icontains=query)
            content_filter = Q(content__icontains=query)
            posts = Post.objects.filter(title_filter | content_filter)

        post_serializer = PostSearchRequestSerializer(posts, many=True)
        return JsonResponse(post_serializer.data, safe=False)
