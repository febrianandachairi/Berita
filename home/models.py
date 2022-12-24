from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helpers import *


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)


class BeritaModel(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    user = models.ForeignKey(User, blank=True, null=True,
                             on_delete=models.CASCADE)
    image = models.ImageField(upload_to='berita')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(BeritaModel, self).save(*args, **kwargs)

class KategoriBerita(models.Model):
    name = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.name)
        super(KategoriBerita, self).save(*args, **kwargs)
        
class BeritaApiBaru(models.Model):
    title = models.CharField(max_length=1000)
    link = models.URLField(max_length=1000, null=True, blank=True)
    contentSnippet = models.TextField()
    isoDate = models.CharField(max_length=1000)
    image = models.URLField(max_length=1000, null=True, blank=True)
    kategori = models.ForeignKey(KategoriBerita,on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(BeritaApiBaru, self).save(*args, **kwargs)
        
