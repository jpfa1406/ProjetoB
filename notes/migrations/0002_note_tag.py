# Generated by Django 3.1.7 on 2021-03-25 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='tag',
            field=models.CharField(max_length=100, null=True),
        ),
    ]