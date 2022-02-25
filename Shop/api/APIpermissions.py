from rest_framework.permissions import BasePermission



class UserCustomPerm(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.id
