from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.template.defaultfilters import slugify
import random
import string


class Categories(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Blog(models.Model):
    blog_title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    category = models.ForeignKey(
        Categories, on_delete=models.SET_NULL, null=True, related_name="category")
    posted_date = models.DateField(default=date.today)
    is_public = models.BooleanField(default=True)
    slug = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.blog_title + " ==> " + str(self.author)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(
                self.blog_title + " " + self.author.username + " " + self.category.category_name)
            self.slug = base_slug + \
                " " .join(random.choice(string.ascii_letters + string.digits)
                          for _ in range(5))
        return super().save(*args, **kwargs)


class BlogComment (models.Model):
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True),
    comment_date = models.DateTimeField(auto_now_add=True),
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.blog)
