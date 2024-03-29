# Generated by Django 2.2.28 on 2023-03-21 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookShare', '0028_merge_20230321_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='interest',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookShare.Book'),
        ),
    ]
