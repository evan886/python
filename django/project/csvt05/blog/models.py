from django.db import models

sex_choices=(
    ('f','famale'),
    ('m','male'),
)
class User(models.Model):
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=1, choices=sex_choices)


