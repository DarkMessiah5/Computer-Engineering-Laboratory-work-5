from django.db import models

# Create your models here.

AVAILABLE_MARKS = (
    ('-', '-'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5')
)


class Student(models.Model):
    name = models.CharField(max_length=127, default='')
    programing_mark = models.CharField(max_length=127, choices=AVAILABLE_MARKS, default=AVAILABLE_MARKS[0][0])
    informatics_mark = models.CharField(max_length=127, choices=AVAILABLE_MARKS, default=AVAILABLE_MARKS[0][0])
    math_mark = models.CharField(max_length=127, choices=AVAILABLE_MARKS, default=AVAILABLE_MARKS[0][0])
    discrete_math_mark = models.CharField(max_length=127, choices=AVAILABLE_MARKS, default=AVAILABLE_MARKS[0][0])
    history_mark = models.CharField(max_length=127, choices=AVAILABLE_MARKS, default=AVAILABLE_MARKS[0][0])

