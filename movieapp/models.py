from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Snippet(models.Model):
    user = models.ForeignKey(User,
                             default=1,
                             null=True,
                             on_delete=models.SET_NULL
                             )
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=400)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    actors = models.CharField(max_length=250)
    averagerating = models.FloatField(default=0)
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
class Review(models.Model):
    movie = models.ForeignKey(Snippet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.user.username