# Generated by Django 5.0.6 on 2024-08-24 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_moviesdata_genere_alter_moviesdata_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesdata',
            name='genere',
            field=models.CharField(max_length=100),
        ),
    ]
