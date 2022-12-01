# coding=utf-8

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from core.models import Base


class Category(Base):
    slug = models.SlugField('Slug', editable=False,
                            unique=True, max_length=200)
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Through this module we can perform several procedures at the 
        moment we the same is being created, such as:
        delete, write, edit, generate audit data in another table, etc.
        """
        if not self.slug:
            slug = f'{slugify(self.name)}'
            self.slug = slug

        return super().save(*args, **kwargs)


class Recipe(Base):
    title = models.CharField('Title', blank=False, unique=True, max_length=65)
    description = models.CharField(
        'Description', blank=False, unique=True, max_length=165)
    slug = models.SlugField('Slug', editable=False,
                            unique=True, max_length=200)
    preparation_time = models.IntegerField('Preparation Time', blank=False)
    preparation_time_unit = models.CharField(
        'Preparation Time Unit.', blank=False, unique=True, max_length=65
    )
    servings = models.IntegerField('Servings', blank=False)
    servings_unit = models.CharField('Servings Unit.', max_length=65)
    preparation_steps = models.TextField('Preparation Steps', blank=False)
    preparation_steps_is_html = models.BooleanField(
        'Preparation Steps Html ', default=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to='recipes/covers/%Y/%m/%d/', blank=False, null=False)

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipes:recipe', args=(self.id,))

    def save(self, *args, **kwargs):
        """
        Through this module we can perform several procedures at the 
        moment we the same is being created, such as:
        delete, write, edit, generate audit data in another table, etc.
        """
        if not self.slug:
            slug = f'{slugify(self.title)}'
            self.slug = slug

        return super().save(*args, **kwargs)
