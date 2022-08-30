from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class ArticleSource(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    source = models.ForeignKey(ArticleSource, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    def __str__(self) -> str:
        return self.text

class Article(models.Model):
    title = models.CharField(max_length=1024)
    content = HTMLField()
    source = models.ForeignKey(ArticleSource,on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    tags = models.ManyToManyField(Tag, verbose_name=("tag"))
    def __str__(self) -> str:
        return self.title