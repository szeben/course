from django.db import models

# Create your models here.
class Courses(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    course = models.ForeignKey(Courses, related_name='reviews', on_delete='CASCADE')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True, default='')
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
 