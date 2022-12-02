from django.db import models

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.caption}"


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(null=False, unique=True)
    content = models.TextField()
    tags = models.ManyToManyField(
        Tag, blank=True, null=True, related_name="posts")
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=False, related_name="posts")

    def __str__(self):
        return f"{self.date} - {self.title}"
