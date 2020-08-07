from rest_framework import generics
from rest_framework.decorators import (
    action,
    api_view,
    authentication_classes,
    renderer_classes,
)
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Post
from .permissions import IsAuthorOrReadonly
from .serializers import PostSerializer

# class PublicPostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.filter(is_public=True)
#     serializer_class = PostSerializer


# class PublicPostListAPIView(APIView):
#     def get(self, request):
#         qs = Post.objects.filter(is_public=True)
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)


# public_post_list = PublicPostListAPIView.as_view()


# @api_view(["GET"])
# def public_post_list(request):
#     qs = Post.objects.filter(is_public=True)
#     serializer = PostSerializer(qs, many=True)
#     return Response(serializer.data)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # DRF Permission
    # IsAuthenticated : 인증된 요청에 한해서, 뷰 호출 허용
    # IsAdminUser : Staff 인증 요청에 한해서, 뷰 호출 허용
    # IsAuthenticatedOrReadOnly : 비 인증 요청에는 읽기 권한만 허용
    # AllowAny(디폴트): 인증 여부에 상관없이, 뷰 호출 허용
    permission_classes = [
        IsAuthorOrReadonly  # Customizing permission Class : 해당 Post의 Author 만 수정가능.
    ]

    # authentication_classes = []  # 인증이 되어있음을 보장받을 수 있음.

    filter_backends = [SearchFilter, OrderingFilter]
    # ?search= : QuerySet 조건 절에 추가할 필드 지정. 모델 필드 중에 문자열 필드만을 지정
    # "^" : Starts-with search 시작하는 패턴에 대해서만
    # "=" : Exact matches 정확하게 일치
    # "@" : Full-text search (2020년 2월 Django Mysql 백엔드만 지원) 모든 문자열 일치
    # "$" : Regex search 정규표현식 서치
    search_fields = ["^message"]
    # ?ordering= : 정렬을 허용할 필드의 화이트리스트. 미지정 시 serializer_class에 지정된 필드들.
    ordering_fileds = ["id"]
    # 디폴트 정렬 지정
    ordering = ["id"]

    def perform_create(self, serializer):
        # FIXME: 인증이 되어있다는 가정하애, author를 지정.
        author = self.request.user  # User or AnonymousUser
        ip = self.request.META["REMOTE_ADDR"]
        serializer.save(ip=ip, author=author)

    @action(detail=False, methods=["GET"])
    def public(self, request):
        qs = self.get_queryset().filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["PATCH"])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save(update_fields=["is_public"])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # ModelViewSet에 해당 Function들이 추상화 되어있음.ㅂ
    # def list(self, request, *args, **kwargs):
    #     pass

    # def create(self, request, *args, **kwargs):
    #     pass

    # def retrieve(self, request, *args, **kwargs):
    #     pass

    # def update(self, request, *args, **kwargs):
    #     pass

    # def partial_update(self, request, *args, **kwargs):
    #     pass

    # def destroy(self, request, *args, **kwargs):
    #     pass

    # def dispatch(self, request, *args, **kwargs):
    #     print("request.body :", request.body)  # print 비추, logger cncjs
    #     print("request.POST :", request.POST)
    #     return super().dispatch(request, *args, **kwargs)


# def post_list(request):
#     # request.method # => 2개분기
#     # GET, POST
#     pass


# def post_detail(request, pk):
#     # request.method # => 3개 분기
#     # GET, PUT, DELETE
#     pass


class PostDetailApiView(RetrieveAPIView):
    queryset = Post.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "instagram/post_detail.html"

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        serializer = PostSerializer(post)
        return Response({"post": serializer.data})
