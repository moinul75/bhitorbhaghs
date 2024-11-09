# Generated by Django 5.1.3 on 2024-11-10 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_examresult_total_boys_examresult_total_girls'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntroductionSchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('school_elln', models.CharField(blank=True, max_length=255, null=True)),
                ('school_name_bn', models.CharField(blank=True, max_length=255, null=True)),
                ('school_name_en', models.CharField(blank=True, max_length=255, null=True)),
                ('village_or_road', models.CharField(blank=True, max_length=255, null=True)),
                ('word_no', models.CharField(blank=True, max_length=50, null=True)),
                ('post_office', models.CharField(blank=True, max_length=255, null=True)),
                ('police_station', models.CharField(blank=True, max_length=255, null=True)),
                ('district', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile_no', models.CharField(blank=True, max_length=15, null=True)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('school_shit', models.CharField(blank=True, max_length=255, null=True)),
                ('school_activites', models.CharField(blank=True, max_length=255, null=True)),
                ('total_land', models.CharField(blank=True, max_length=50, null=True)),
                ('total_classroom', models.CharField(blank=True, max_length=50, null=True)),
                ('total_ict_lab', models.CharField(blank=True, max_length=50, null=True)),
                ('total_library_room', models.CharField(blank=True, max_length=50, null=True)),
                ('has_boundary', models.BooleanField(blank=True, null=True)),
                ('has_playground', models.BooleanField(blank=True, null=True)),
                ('union_city_corparation', models.CharField(blank=True, max_length=255, null=True)),
                ('post_code', models.CharField(blank=True, max_length=10, null=True)),
                ('upozila', models.CharField(blank=True, max_length=255, null=True)),
                ('division', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('total_students', models.CharField(blank=True, max_length=50, null=True)),
                ('school_chars', models.CharField(blank=True, max_length=255, null=True)),
                ('total_vobon', models.CharField(blank=True, max_length=50, null=True)),
                ('total_multimedia_room', models.CharField(blank=True, max_length=50, null=True)),
                ('total_room_for_science', models.CharField(blank=True, max_length=50, null=True)),
                ('has_auditorium', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]