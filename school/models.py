from django.db import models

class student(models.Model):
  name = models.CharField(max_length=30)
  rg = models.CharField(max_length=9)
  cpf = models.CharField(max_length=11)
  birth_date = models.DateField()

  def __str__(self):
    return self.name

class course(models.Model):
  LEVEL = (
    ('B', 'Basic'),
    ('I', 'Intermediary'),
    ('A', 'Advanced'),
  )

  course_code = models.CharField(max_length=30)
  description = models.CharField(max_length=100)
  course_level = models.CharField(max_length=1, choices=LEVEL, blank=False, null=False, default='B')

  def __str__(self):
    return self.description