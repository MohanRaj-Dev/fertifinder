# Generated by Django 5.0.3 on 2024-04-04 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_remove_fertilizer_nitro_phosphate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fertilizer',
            name='image',
            field=models.ImageField(default='ok.jpg', upload_to=''),
        ),
    ]
