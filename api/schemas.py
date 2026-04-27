from ninja import Schema
from typing import Optional

# =====================
# AUTH
# =====================

class RegisterSchema(Schema):
    username: str
    password: str
    role: str


class LoginSchema(Schema):
    username: str
    password: str


class TokenSchema(Schema):
    access: str
    refresh: str


# =====================
# COURSE
# =====================

# 👉 untuk CREATE / UPDATE
class CourseInSchema(Schema):
    title: str
    description: Optional[str] = None


# 👉 untuk RESPONSE (WAJIB ADA id)
class CourseOutSchema(Schema):
    id: int
    title: str
    description: Optional[str] = None


# =====================
# ENROLLMENT
# =====================

class EnrollmentSchema(Schema):
    course_id: int

class UserOutSchema(Schema):
    id: int
    username: str
    role: str

class UpdateUserSchema(Schema):
    username: Optional[str] = None
    password: Optional[str] = None

class EnrollmentOutSchema(Schema):
    id: int
    course_id: int
    student_id: int