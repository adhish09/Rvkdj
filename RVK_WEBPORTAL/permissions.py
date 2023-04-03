from rest_framework.permissions import DjangoModelPermissions, BasePermission


class ReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        return False