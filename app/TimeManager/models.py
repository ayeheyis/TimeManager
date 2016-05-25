from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Task(models.Model):
    #Basic description of the task
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    expected_duration = models.IntegerField(blank=True, default=-1)
    actual_duration = models.IntegerField(blank=True, default=-1)

    #Importance of task
    PRIORITY_LEVELS = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
                       ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'))
    priority = models.CharField(max_length=1, choices=PRIORITY_LEVELS)

    #Group identifiers
    category = models.ForeignKey(Category)
    group_id = models.IntegerField(blank=True, default=-1)
    course = models.ForeignKey(Course, null=True, blank=True)

    def __unicode__(self):
        return self.name