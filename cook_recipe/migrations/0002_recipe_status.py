# Generated by Django 3.2.22 on 2023-10-11 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cook_recipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]
