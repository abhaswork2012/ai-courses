from django.core.validators import MinValueValidator
from django.db import models
class Author(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Member(models.Model):
    name = models.CharField(max_length=200)
    joined_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class MemberCard(models.Model):
    member = models.OneToOneField(
        Member, on_delete=models.CASCADE, related_name="card"
    )
    serial = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return f"Card {self.serial}"
class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, related_name="books")
    replacement_cost = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[MinValueValidator(0)]
    )
    copies = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    added_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title} (${self.replacement_cost:.2f})"
class Loan(models.Model):
    member = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name="loans"
    )
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name="loans")
    due_date = models.DateField()
    returned = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.book.title} -> {self.member.name} (due {self.due_date})"