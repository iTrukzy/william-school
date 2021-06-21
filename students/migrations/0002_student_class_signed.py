# Generated by Django 2.2.24 on 2021-06-20 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_remove_class_students'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='class_signed',
            field=models.ManyToManyField(related_name='students', to='classes.Class'),
        ),
    ]