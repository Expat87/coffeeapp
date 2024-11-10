# Generated by Django 3.2.25 on 2024-11-07 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_rename_ratings_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffeeshop',
            name='coffeeshop_status',
            field=models.CharField(choices=[('A', 'Active'), ('C', 'Closed')], default='A', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coffeeshop',
            name='coffeeshop_address',
            field=models.CharField(max_length=100),
        ),
    ]