# Generated by Django 3.2.18 on 2023-04-27 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='door',
            name='description',
            field=models.TextField(max_length=255, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='door',
            name='tech_info',
            field=models.TextField(verbose_name='Техническое описание'),
        ),
    ]
