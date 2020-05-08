from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=30, verbose_name='Group')
    students = models.ManyToManyField(User)

class Task(models.Model):
    name = models.CharField(max_length=100, verbose_name='Task name')
    creation_date = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(verbose_name='Deadline')
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, verbose_name='Group', blank=False, null=True)
    title = models.CharField(max_length=100, verbose_name='Title')
    words_number = models.PositiveSmallIntegerField(verbose_name='Words number')
    paragraph_number = models.PositiveSmallIntegerField(verbose_name='Paragraph number')


class Work(models.Model):
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, verbose_name='Task', blank=False, null=True)
    student = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Student', blank=False, null=True)
    text = models.TextField(verbose_name='Text')
    words_number = models.PositiveSmallIntegerField(verbose_name='Words number')
    paragraph_number = models.PositiveSmallIntegerField(verbose_name='Paragraph number')

    


class Articles(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author', blank=True, null=True)
    creation_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, verbose_name='Name')
    text = models.TextField(verbose_name='Text')

    def __str__(self):
        return f'{self.name}_{self.creation_date}'

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class Essay(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    creation_date = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name='Text')

    def __str__(self):
        return f'{self.name}_{self.creation_date}'

    class Meta:
        verbose_name = 'Essay'
        verbose_name_plural = 'Essays'