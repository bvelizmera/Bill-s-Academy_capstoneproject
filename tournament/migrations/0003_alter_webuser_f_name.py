# Generated by Django 4.2.11 on 2024-03-20 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0002_alter_webuser_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webuser',
            name='f_name',
            field=models.CharField(max_length=50),
        ),
    ]