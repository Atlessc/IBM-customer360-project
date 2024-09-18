from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Question, Choice, Submission, Enrollment

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    enrollment = Enrollment.objects.get(user=request.user, course=course)
    submission = Submission.objects.create(enrollment=enrollment)
    selected_choices = request.POST.getlist('choices')
    for choice_id in selected_choices:
        choice = get_object_or_404(Choice, pk=int(choice_id))
        submission.choices.add(choice)
    submission.save()
    return redirect('show_exam_result', course_id=course.id, submission_id=submission.id)

def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    selected_ids = submission.choices.values_list('id', flat=True)
    total_score = sum([question.grade for question in course.question_set.all() if question.is_get_score(selected_ids)])
    context = {
        'course': course,
        'submission': submission,
        'total_score': total_score,
    }
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)

def course_detail(request, course_id):
    # Fetch the course using the course_id or return a 404 if not found
    course = get_object_or_404(Course, pk=course_id)
    # Render the course details page with the course data
    return render(request, 'onlinecourse/course_details_bootstrap.html', {'course': course})
