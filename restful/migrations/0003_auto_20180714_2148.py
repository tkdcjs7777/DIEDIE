# Generated by Django 2.0.7 on 2018-07-14 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0002_ranking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ranking',
            name='clear_time',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
