from django.db import models

# models.py

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
        ('Database', 'Database'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Frontend')
    icon = models.ImageField(upload_to='icons/', default='icons/default_icon.png')
    

    def __str__(self):
        return self.name
class Project(models.Model):
    TECHNOLOGY_CHOICES = [
        ('HTML', 'HTML'),
        ('CSS', 'CSS'),
        ('Javascript', 'JavaScript'),
        ('React', 'React'),
        ('Node.js', 'Node.js'),
        ('Django', 'Django'),
    ]
    name = models.CharField(default="",max_length=100)
    description = models.TextField(default='Add description here')
    image = models.ImageField(upload_to='project_images/',default='project_images/default_icon.png')
    link = models.URLField(default="")
    technologies = models.CharField(max_length=50, choices=TECHNOLOGY_CHOICES, default='')  # Example: Django, HTML, CSS, JavaScript, React, Node.js, etc.

    def __str__(self):
        return self.name

class Document(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

