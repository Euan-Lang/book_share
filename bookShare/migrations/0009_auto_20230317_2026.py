# Generated by Django 2.2.28 on 2023-03-17 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookShare', '0008_auto_20230317_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='book_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookShare.Book'),
        ),
    ]
