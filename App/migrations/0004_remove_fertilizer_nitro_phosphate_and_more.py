# Generated by Django 5.0.3 on 2024-04-04 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_fertilizer_dap_fertilizer_muriate_of_potash_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fertilizer',
            name='nitro_phosphate',
        ),
        migrations.RemoveField(
            model_name='fertilizer',
            name='sugar_phosphate',
        ),
    ]
