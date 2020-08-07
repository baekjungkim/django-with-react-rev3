from rest_framework import permissions

# Author 가 있다는 경우
class IsAuthorOrReadonly(permissions.BasePermission):

    # 인증이 되어야만, 목록조회/ 포스팅 등록을 허용
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    # Detail Post 해당
    def has_object_permission(self, request, view, obj):

        # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
        # 해당 method 호출시 True
        if request.method in permissions.SAFE_METHODS:
            return True

        # 프로젝트에 따라 유동적
        # 해당 Post 의 작성자가 아니면 false
        return obj.author == request.user
