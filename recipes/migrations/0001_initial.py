# Generated by Django 4.1.1 on 2022-09-25 21:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Time')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Entry date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create at')),
                ('slug', models.SlugField(editable=False, max_length=200, unique=True, verbose_name='Slug')),
                ('name', models.CharField(max_length=65)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Time')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Entry date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create at')),
                ('title', models.CharField(max_length=65, unique=True, verbose_name='Title')),
                ('description', models.CharField(max_length=165, unique=True, verbose_name='Description')),
                ('slug', models.SlugField(editable=False, max_length=200, unique=True, verbose_name='Slug')),
                ('preparation_time', models.IntegerField(verbose_name='Preparation Time')),
                ('preparation_time_unit', models.CharField(max_length=65, unique=True, verbose_name='Preparation Time Unit.')),
                ('servings', models.IntegerField(verbose_name='Servings')),
                ('servings_unit', models.CharField(max_length=65, verbose_name='Servings Unit.')),
                ('preparation_steps', models.TextField(verbose_name='Preparation Steps')),
                ('preparation_steps_is_html', models.BooleanField(default=False, verbose_name='Preparation Steps Html ')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False)),
                ('cover', models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recipes.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
