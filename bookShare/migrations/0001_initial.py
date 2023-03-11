# Generated by Django 2.2.28 on 2023-03-05 20:10

import bookShare.models
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
            name='Author',
            fields=[
                ('author_id', models.AutoField(primary_key=True, serialize=False)),
                ('author_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('publisher_id', models.AutoField(primary_key=True, serialize=False)),
                ('publisher_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=128)),
                ('post_code', models.CharField(max_length=6)),
                ('phone_number', models.CharField(max_length=11)),
                ('joined_date', models.DateField(auto_now_add=True)),
                ('reputation', models.IntegerField()),
                ('user_image', models.ImageField(blank=True, null=True, upload_to=bookShare.models.rename_user)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]