from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post


# def post_list(request):
#     # request.method # => 2개분기
#     # GET, POST
#     pass


# def post_detail(request, pk):
#     # request.method # => 3개 분기
#     # GET, PUT, DELETE
#     pass


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def dispatch(self, request, *args, **kwargs):
    #     print("request.body :", request.body)  # print 비추, logger cncjs
    #     print("request.POST :", request.POST)
    #     return super().dispatch(request, *args, **kwargs)

