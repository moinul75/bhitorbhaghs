# Generated by Django 5.1 on 2024-09-04 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_gallary_options_socialmedia_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='icon_class',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]