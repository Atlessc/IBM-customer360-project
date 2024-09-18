from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name  # This will display the course name

class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    grade = models.IntegerField(default=1)

    def __str__(self):
        return self.text  # This will display the question text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text  # This will display the choice text

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.name}"

class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)

    def __str__(self):
        return f"Submission by {self.enrollment.user.username} for {self.enrollment.course.name}"
