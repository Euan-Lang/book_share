# Generated by Django 2.2.28 on 2023-03-21 11:09

import bookShare.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookShare', '0023_merge_20230320_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookShare.Book'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_image',
            field=models.ImageField(blank=True, null=True, upload_to=bookShare.models.rename_user),
        ),
    ]
