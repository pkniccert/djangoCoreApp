# Generated by Django 5.1 on 2024-08-19 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customuser_managers_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='user_23764b43', max_length=150, unique=True),
        ),
    ]
