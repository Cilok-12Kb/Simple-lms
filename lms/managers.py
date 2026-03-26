from django.db import models

class CourseQuerySet(models.QuerySet):
    def for_listing(self):
        return self.select_related('instructor', 'category') \
                   .prefetch_related('lessons')

class EnrollmentQuerySet(models.QuerySet):
    def for_student_dashboard(self):
        return self.select_related('course', 'course__instructor') \
                   .prefetch_related('course__lessons')
    
