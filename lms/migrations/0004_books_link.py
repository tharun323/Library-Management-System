# Generated by Django 2.0.4 on 2018-04-13 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0003_auto_20180412_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='link',
            field=models.CharField(default='foobar', max_length=150),
        ),
    ]
