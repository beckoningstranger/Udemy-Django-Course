from django.db import models

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=20)


class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=50)
    date = models.DateField()
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    content = models.CharField(max_length=2000)
    tag = models.ManyToManyField(Tag, null=True, related_name="posts")

    def __str__(self):
        return f"{self.date} - {self.title}"


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_address = models.EmailField
    posts = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=False, related_name="author")

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
