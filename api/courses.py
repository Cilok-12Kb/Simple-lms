from ninja import Router
from lms.models import Course
from ninja.pagination import paginate
from typing import List
from ninja.errors import HttpError
from .permissions import get_current_user, instructor_required, admin_required
from .schemas import CourseInSchema, CourseOutSchema

router = Router()


# =====================
# PUBLIC
# =====================

@router.get("/", response=List[CourseOutSchema])
@paginate
def list_courses(request, title: str = None):
    qs = Course.objects.all()

    if title:
        qs = qs.filter(title__icontains=title)

    return qs


@router.get("/{id}", response=CourseOutSchema)
def detail_course(request, id: int):
    return Course.objects.get(id=id)


# =====================
# PROTECTED
# =====================

@router.post("/", response=CourseOutSchema)
@instructor_required
def create_course(request, data: CourseInSchema):
    user = get_current_user(request)

    return Course.objects.create(
        title=data.title,
        description=data.description,
        instructor=user
    )


@router.patch("/{id}", response=CourseOutSchema)
@instructor_required
def update_course(request, id: int, data: CourseInSchema):
    user = get_current_user(request)
    course = Course.objects.get(id=id)

    if course.instructor != user:
        raise HttpError(403, "Not owner")

    course.title = data.title or course.title
    course.description = data.description or course.description
    course.save()

    return course


@router.delete("/{id}")
@admin_required
def delete_course(request, id: int):
    Course.objects.get(id=id).delete()
    return {"success": True}