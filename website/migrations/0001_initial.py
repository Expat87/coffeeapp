# Generated by Django 3.2.25 on 2024-11-07 07:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coffeeshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('coffeeshop_name', models.CharField(max_length=100)),
                ('coffeeshop_address', models.CharField(choices=[('A', 'Active'), ('C', 'Closed')], max_length=1)),
                ('created_by', models.ForeignKey(limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('size', models.CharField(choices=[('S', 'Small'), ('L', 'Large'), ('W', 'Weird Milk')], max_length=1)),
                ('pirce', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Transaction Amount')),
                ('description', models.TextField(blank=True)),
                ('coffeeshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.coffeeshop')),
                ('created_by', models.ForeignKey(limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
