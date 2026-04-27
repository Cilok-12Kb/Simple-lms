from ninja import Router
from lms.models import Enrollment, Course
from .permissions import get_current_user, student_required
from .schemas import EnrollmentSchema, EnrollmentOutSchema
from ninja.errors import HttpError
from typing import List

router = Router()


@router.post("/", response=EnrollmentOutSchema)
@student_required
def enroll(request, data: EnrollmentSchema):
    user = get_current_user(request)

    course = Course.objects.get(id=data.course_id)

    enrollment = Enrollment.objects.create(
        student=user,
        course=course
    )

    return enrollment


@router.get("/my-courses", response=List[EnrollmentOutSchema])
def my_courses(request):
    user = get_current_user(request)
    return Enrollment.objects.filter(student=user)


@router.post("/{id}/progress")
def mark_progress(request, id: int):
    user = get_current_user(request)

    enrollment = Enrollment.objects.get(id=id)

    if enrollment.student != user:
        raise HttpError(403, "Not your enrollment")

    enrollment.completed = True
    enrollment.save()

    return {"message": "Progress updated"}