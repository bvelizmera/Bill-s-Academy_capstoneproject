# Generated by Django 4.2.11 on 2024-03-22 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webuser',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]
