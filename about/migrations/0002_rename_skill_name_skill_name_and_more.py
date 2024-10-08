# Generated by Django 5.0.7 on 2024-08-14 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='skill_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='skill_origin',
        ),
        migrations.AddField(
            model_name='interest',
            name='description',
            field=models.TextField(default='Description is not available when no interest was added'),
            preserve_default=False,
        ),
    ]
