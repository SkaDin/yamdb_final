# Generated by Django 3.2.17 on 2023-02-11 23:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import reviews.validators


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
                ('name', models.CharField(max_length=256, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Категория',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Жанр',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Наименование произведения')),
                ('year', models.SmallIntegerField(db_index=True, validators=[reviews.validators.validator_year], verbose_name='Год выпуска')),
                ('description', models.TextField(verbose_name='Описание')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='reviews.category', verbose_name='Категория')),
                ('genre', models.ManyToManyField(db_index=True, related_name='titles', to='reviews.Genre', verbose_name='Жанр')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text='Опишите свои впечатления:', max_length=400, verbose_name='Текст комментария:')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации:')),
                ('score', models.IntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'), (6, 'six'), (7, 'seven'), (8, 'eight'), (9, 'nine'), (10, 'ten')])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='reviews.title', verbose_name='Произведения:')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=400, verbose_name='Текст отзыва:')),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации:')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор отзыва:')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='reviews.review')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('author', 'title'), name='Review from this author already exist.'),
        ),
    ]
