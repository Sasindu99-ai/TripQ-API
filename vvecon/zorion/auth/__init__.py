from functools import wraps

from rest_framework import status
from rest_framework.response import Response

from .JWTProvider import JWTProvider

__all__ = ['Authorized', 'JWTProvider']


def Authorize(func):

    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({'message': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        return func(self, request, *args, **kwargs)

    wrapper.authorized = True
    return wrapper


Authorized = Authorize
