from ninja import Router
from django.contrib.auth import authenticate
from lms.models import User
from .schemas import RegisterSchema, LoginSchema
from .jwt import create_access_token, create_refresh_token,  decode_token
from .permissions import get_current_user
from .schemas import RegisterSchema, LoginSchema, UpdateUserSchema, UserOutSchema
from ninja.errors import HttpError

router = Router()

@router.post("/register", auth=None)
def register(request, data: RegisterSchema):
    user = User.objects.create_user(
        username=data.username,
        password=data.password,
        role=data.role
    )
    return {"message": "User created"}


@router.post("/login", auth=None)
def login(request, data: LoginSchema):
    user = authenticate(username=data.username, password=data.password)

    if not user:
        return {"error": "Invalid credentials"}

    return {
        "access": create_access_token(user.id),
        "refresh": create_refresh_token(user.id)
    }

@router.get("/me", response=UserOutSchema)
def me(request):
    user = request.auth

    if not user:
        raise HttpError(401, "Unauthorized")

    return user

@router.put("/me", response=UserOutSchema)
def update_me(request, data: UpdateUserSchema):
    user = request.auth

    if not user:
        raise HttpError(401, "Unauthorized")

    if data.username:
        user.username = data.username

    user.save()

    return user

@router.post("/refresh")
def refresh(request, refresh_token: str):
    try:
        payload = decode_token(refresh_token)
        user_id = payload["user_id"]

        return {
            "access": create_access_token(user_id)
        }
    except:
        return {"error": "Invalid refresh token"}