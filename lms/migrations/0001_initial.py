# Generated by Django 2.0.4 on 2018-04-12 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('author_name', models.CharField(max_length=100)),
                ('no_of_books', models.IntegerField()),
                ('book_image', models.ImageField(blank=True, upload_to='book_image')),
            ],
        ),
    ]
