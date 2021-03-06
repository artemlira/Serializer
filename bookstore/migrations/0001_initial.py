# Generated by Django 3.0.8 on 2020-07-03 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=48)),
                ('last_name', models.CharField(max_length=48)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48)),
                ('address', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=128)),
                ('site', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('publication_date', models.DateField()),
                ('authors', models.ManyToManyField(to='bookstore.Author')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.Publisher')),
            ],
        ),
    ]
