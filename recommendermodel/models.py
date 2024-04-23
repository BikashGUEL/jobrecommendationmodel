from django.db import models

class Student(models.Model):
    student_id = models.TextField(max_length=200, primary_key=True)
    print(student_id)
    student_tags = models.TextField()

    class Meta:
        db_table = 'student_tb'

class Job(models.Model):
    job_title = models.TextField(max_length=200, primary_key=True)
    job_tags = models.TextField()

    class Meta:
        db_table = 'job_tb'