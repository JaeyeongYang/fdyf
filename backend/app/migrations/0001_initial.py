# Generated by Django 3.2.9 on 2021-11-17 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Ingredients ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='재료명')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='메뉴 수')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Menu ID')),
                ('name', models.CharField(max_length=200, verbose_name='메뉴명')),
                ('way', models.CharField(max_length=100, null=True, verbose_name='조리방법')),
                ('pat', models.CharField(max_length=100, null=True, verbose_name='조리종류')),
                ('energy', models.FloatField(verbose_name='열량')),
                ('carb', models.FloatField(verbose_name='탄수화물')),
                ('protein', models.FloatField(verbose_name='단백질')),
                ('fat', models.FloatField(verbose_name='지방')),
                ('na', models.FloatField(verbose_name='나트륨')),
                ('hashtag', models.CharField(max_length=100, null=True, verbose_name='해시태그')),
                ('img_small', models.URLField(verbose_name='이미지경로(소)')),
                ('img_large', models.URLField(verbose_name='이미지경로(대)')),
                ('ingredients', models.TextField(verbose_name='재료정보')),
                ('ingredients_count', models.PositiveIntegerField(default=0, verbose_name='재료 수')),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ingredient')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.menu')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Recipe ID')),
                ('order', models.PositiveSmallIntegerField(verbose_name='순서')),
                ('text', models.TextField(verbose_name='만드는 법')),
                ('img', models.URLField(verbose_name='이미지경로')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='app.menu', verbose_name='조리메뉴')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='ingredients_set',
            field=models.ManyToManyField(related_name='menus', through='app.Requirement', to='app.Ingredient'),
        ),
    ]
