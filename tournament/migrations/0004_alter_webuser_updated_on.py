# Generated by Django 4.2.11 on 2024-03-20 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0003_alter_webuser_f_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webuser',
            name='updated_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]