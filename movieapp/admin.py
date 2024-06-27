from django.contrib import admin
from .models import Snippet,Review,Category


# Register your models here.
admin.site.register(Snippet)
admin.site.register(Review)
admin.site.register(Category)

