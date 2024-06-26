# Generated by Django 4.2.1 on 2024-05-26 17:25

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
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100)),
                ('area', models.PositiveIntegerField()),
                ('bedrooms', models.PositiveIntegerField()),
                ('bathrooms', models.PositiveIntegerField()),
                ('hospitals_nearby', models.TextField(blank=True, null=True)),
                ('colleges_nearby', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('is_seller', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_properties', to='app.userprofile')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.property')),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='app.userprofile'),
        ),
        migrations.CreateModel(
            name='InterestedBuyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interested_properties', to='app.userprofile')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.property')),
            ],
        ),
    ]
