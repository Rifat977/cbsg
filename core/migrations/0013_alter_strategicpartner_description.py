# Generated by Django 5.1.6 on 2025-03-15 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_rename_our_mission_text_about_our_mission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strategicpartner',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
