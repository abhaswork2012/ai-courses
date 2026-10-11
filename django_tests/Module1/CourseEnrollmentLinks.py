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
    # Write your code here
    class Meta:
        ordering = ["name"]
    def __str__(self):
        return self.name
class Transcript(models.Model):
    # Write your code here
    gpa = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    class Meta:
        ordering = ["pk"]
    def __str__(self):
        return f"Transcript #{self.pk}"