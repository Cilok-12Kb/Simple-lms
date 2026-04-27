from django.http import JsonResponse
from django.db.models import Count, Avg, Max, Min
from .models import Course, User, Category, Lesson

# =========================
# 🔴 BASELINE
# =========================
def course_list_baseline(request):
    courses = Course.objects.all()
    data = []

    for c in courses:
        data.append({
            'course': c.title,
            'teacher': c.instructor.username,  # N+1
        })

    return JsonResponse({'data': data})


# =========================
# ✅ OPTIMIZED
# =========================
def course_list_optimized(request):
    courses = Course.objects.select_related('instructor').all()
    data = []

    for c in courses:
        data.append({
            'course': c.title,
            'teacher': c.instructor.username,
        })

    return JsonResponse({'data': data})


# =========================
# 🔴 BASELINE
# =========================
def course_members_baseline(request):
    courses = Course.objects.all()
    data = []

    for c in courses:
        data.append({
            'course': c.title,
            'member_count': c.enrollment_set.count(),  # N+1
        })

    return JsonResponse({'data': data})


# =========================
# ✅ OPTIMIZED
# =========================
def course_members_optimized(request):
    courses = Course.objects.prefetch_related('enrollment_set').all()
    data = []

    for c in courses:
        data.append({
            'course': c.title,
            'member_count': len(c.enrollment_set.all()),
        })

    return JsonResponse({'data': data})


# =========================
# 🔴 BASELINE
# =========================
def course_dashboard_baseline(request):
    courses = Course.objects.all()

    total = courses.count()

    if total == 0:
        return JsonResponse({
            'total': 0,
            'max_price': 0,
            'min_price': 0,
            'avg_price': 0,
        })

    # ⚠️ kamu tidak punya field price → ganti logic
    # contoh: pakai jumlah lesson sebagai "nilai"
    values = [c.lessons.count() for c in courses]

    max_val = max(values)
    min_val = min(values)
    avg_val = sum(values) / total

    return JsonResponse({
        'total': total,
        'max_lessons': max_val,
        'min_lessons': min_val,
        'avg_lessons': avg_val,
    })


# =========================
# ✅ OPTIMIZED
# =========================
def course_dashboard_optimized(request):
    stats = Course.objects.annotate(
        lesson_count=Count('lessons')
    ).aggregate(
        total=Count('id'),
        max_lessons=Max('lesson_count'),
        min_lessons=Min('lesson_count'),
        avg_lessons=Avg('lesson_count'),
    )

    return JsonResponse(stats)

#=======================================================
def bulk_insert_baseline(request):
    course = Course.objects.first()

    for i in range(500):
        Lesson.objects.create(
            course=course,
            title=f'Lesson {i}',
            content='Test',
            order=i
        )

    return JsonResponse({'status': 'baseline done'})

def bulk_insert_optimized(request):
    course = Course.objects.first()

    data = []
    for i in range(500):
        data.append(
            Lesson(
                course=course,
                title=f'Lesson {i}',
                content='Test',
                order=i
            )
        )

    Lesson.objects.bulk_create(data, batch_size=200)

    return JsonResponse({'status': 'optimized done'})

#=========================================
def course_filter(request):
    instructor_id = request.GET.get('instructor')

    courses = Course.objects.filter(instructor_id=instructor_id)

    data = [c.title for c in courses]

    return JsonResponse({'data': data})