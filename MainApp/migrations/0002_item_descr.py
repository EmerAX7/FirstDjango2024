# Generated by Django 5.0.8 on 2024-08-09 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='descr',
            field=models.TextField(default='здесь должно быть описание', max_length=200),
        ),
    ]
