from rest_framework.permissions import BasePermission


class IsTheOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.the_cart.user == request.user
