from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.

class NewsArticle(models.Model):
    headline = models.CharField(max_length=120)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    # date_pub = models.DateField()
    author = models.CharField(max_length=25)
    summary = models.CharField(max_length=150)
    content = models.TextField()

    # Used to create slug field from the headline
    def save(self, *args, **kwargs):
        self.slug = slugify(self.headline)
        super(NewsArticle, self).save(*args, **kwargs)

    def get_slug(self):
        return self.slug
