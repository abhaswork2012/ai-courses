from django.db import models
class Course(models.Model):
    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    class Meta:
        ordering = ["code"]
    def __str__(self):
        return self.code
class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    courses = models.ManyToManyField(
        Course, related_name="students", blank=True
    )
    class Meta:
        ordering = ["name"]
    def __str__(self):
        return self.name
class Transcript(models.Model):
    student = models.OneToOneField(
        Student, on_delete=models.CASCADE, related_name="transcript"
    )
    gpa = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    class Meta:
        ordering = ["pk"]
    def __str__(self):
        return f"Transcript #{self.pk}"

#https://www.staffcoder.com/questions/10057?step=2e5f1c2e-c2a9-4b26-8d8f-7da6ef711009