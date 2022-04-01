from rest_framework import permissions

class IsAutorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # faqatgina ko'rish uchun
        if request.method in permissions.SAFE_METHODS:
            return True
        # o'zgartirish ko'rish ya'ni yozish uchun ruxsatnoma faqatgina post muallifga beriladi
        return obj.author == request.user