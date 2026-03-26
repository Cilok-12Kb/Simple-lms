from lms.models import Course
from django.db import connection, reset_queries


def without_optimization():
    courses = Course.objects.all()

    for course in courses:
        print(course.instructor.username)


def with_optimization():
    courses = Course.objects.select_related('instructor')

    for course in courses:
        print(course.instructor.username)


def compare_queries():
    print("=== TANPA OPTIMASI ===")
    reset_queries()
    without_optimization()
    print("Total Query:", len(connection.queries))

    print("\n=== DENGAN OPTIMASI ===")
    reset_queries()
    with_optimization()
    print("Total Query:", len(connection.queries))