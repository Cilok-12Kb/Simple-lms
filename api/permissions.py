from .jwt import decode_token
from lms.models import User
from functools import wraps


def get_current_user(request):
    auth = request.headers.get("Authorization")

    if not auth:
        return None

    try:
        token = auth.split(" ")[1]
        payload = decode_token(token)
        return User.objects.get(id=payload["user_id"])
    except:
        return None


# =====================
# ROLE CHECK
# =====================

def is_admin(user):
    return user and user.role == "admin"


def is_instructor(user):
    return user and user.role == "instructor"


def is_student(user):
    return user and user.role == "student"


# =====================
# DECORATORS
# =====================

def instructor_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        user = get_current_user(request)
        if not is_instructor(user):
            return {"error": "Instructor only"}
        return func(request, *args, **kwargs)
    return wrapper


def admin_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        user = get_current_user(request)
        if not is_admin(user):
            return {"error": "Admin only"}
        return func(request, *args, **kwargs)
    return wrapper


def student_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        user = get_current_user(request)
        if not is_student(user):
            return {"error": "Student only"}
        return func(request, *args, **kwargs)
    return wrapper