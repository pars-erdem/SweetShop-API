# Generated by Django 5.0.7 on 2024-08-05 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='publish_data',
            field=models.DateField(blank=True, null=True),
        ),
    ]
