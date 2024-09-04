# Generated by Django 5.1 on 2024-09-04 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_gallary_created_at_gallary_updated_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallary',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'Gallary'},
        ),
        migrations.AddField(
            model_name='socialmedia',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='socialmedia',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]