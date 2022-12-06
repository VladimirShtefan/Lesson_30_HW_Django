from rest_framework.permissions import BasePermission


class SelectionOwnerPermission(BasePermission):
    message = 'Вы не являетесь владельцем'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
