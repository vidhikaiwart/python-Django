from django.db import models

# Create your models here.
class Student(models.Model):
    SUBJECT_CHOICES = [
        ('Math', 'Mathematics'),    
        ('Science', 'Science'),
        ('History', 'History'),
        ('Literature', 'Literature'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='student_images/')
    age = models.IntegerField()
    email = models.EmailField()
    type = models.CharField(max_length=20, choices=SUBJECT_CHOICES)

    def __str__(self):
        return self.name