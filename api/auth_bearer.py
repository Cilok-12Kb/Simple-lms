from ninja.security import HttpBearer
from .jwt import decode_token
from lms.models import User

class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        try:
            payload = decode_token(token)
            user = User.objects.get(id=payload["user_id"])
            return user
        except:
            return None