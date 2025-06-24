from rest_framework import permissions, authentication
from services.authentication import TokenAuthentication
from services.permissions import CustomPermissions


class BaseSecurity:
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]