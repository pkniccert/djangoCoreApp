# Generated by Django 5.1 on 2024-08-11 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_alter_recipe_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_descrition',
            field=models.TextField(blank=True, null=True),
        ),
    ]
