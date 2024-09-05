# Generated by Django 5.1 on 2024-09-05 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_classinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAdmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name_bn', models.CharField(max_length=255, verbose_name='শিক্ষার্থীর নাম (বাংলায়)')),
                ('student_name_en', models.CharField(max_length=255, verbose_name='শিক্ষার্থীর নাম (ইংরেজি)')),
                ('father_name_bn', models.CharField(max_length=255, verbose_name='পিতার নাম (বাংলায়)')),
                ('father_name_en', models.CharField(max_length=255, verbose_name='পিতার নাম (ইংরেজি)')),
                ('father_nid', models.CharField(blank=True, max_length=17, null=True, verbose_name='পিতার জাতীয় পরিচয় পত্র নং')),
                ('mother_name_bn', models.CharField(max_length=255, verbose_name='মাতার নাম (বাংলায়)')),
                ('mother_name_en', models.CharField(max_length=255, verbose_name='মাতার নাম (ইংরেজি)')),
                ('mother_nid', models.CharField(blank=True, max_length=17, null=True, verbose_name='মাতার জাতীয় পরিচয় পত্র নং')),
                ('permanent_address', models.TextField(verbose_name='স্থায়ী ঠিকানা')),
                ('present_address', models.TextField(verbose_name='বর্তমান ঠিকানা')),
                ('annual_income', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='পিতা/মাতার বাৎসরিক আয়')),
                ('guardian_mobile', models.CharField(max_length=15, verbose_name='অভিভাবকের মোবাইল নম্বার (ইংরেজি)')),
                ('guardian_occupation', models.CharField(blank=True, max_length=255, null=True, verbose_name='পেশা')),
                ('guardian_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='পিতা মাতার অবর্তমানে বৈধ অভিভাবকের নাম')),
                ('guardian_address', models.TextField(blank=True, null=True, verbose_name='ঠিকানা')),
                ('nationality', models.CharField(default='বাংলাদেশী', max_length=50, verbose_name='জাতীয়তা')),
                ('religion', models.CharField(max_length=50, verbose_name='ধর্ম')),
                ('birth_date', models.DateField(verbose_name='জন্ম তারিখ (mm/dd/yyyy)')),
                ('age', models.IntegerField(verbose_name='বয়স')),
                ('birth_registration_no', models.CharField(blank=True, max_length=17, null=True, verbose_name='জাতীয় জন্ম নিবন্ধন নম্বার')),
                ('previous_school_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='পূর্বে যে বিদ্যালয়ে ছাত্র/ছাত্রী ছিল তাহার নাম')),
                ('previous_class', models.CharField(blank=True, max_length=50, null=True, verbose_name='যে শ্রেণীতে অধ্যায়নরত ছিল')),
                ('last_exam_passed', models.CharField(blank=True, max_length=255, null=True, verbose_name='শেষ যে পরীক্ষায় উত্তীর্ণ হয়েছে তার নাম')),
                ('result_gpa', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='রেজাল্ট(জি.পি.এ)')),
                ('admission_class', models.CharField(max_length=50, verbose_name='যে শ্রেণীতে ভর্তি হতে ইচ্ছুক')),
                ('transfer_certificate_no', models.CharField(blank=True, max_length=50, null=True, verbose_name='ছাড়পত্র নং')),
                ('student_job', models.CharField(blank=True, max_length=255, null=True, verbose_name='ছাত্র/ছাত্রী কোন পেশায় জড়িত থাকলে পেশার নাম')),
                ('quota', models.CharField(blank=True, max_length=50, null=True, verbose_name='কোটা')),
                ('birth_certificate', models.FileField(blank=True, null=True, upload_to='documents/birth-certificate/', verbose_name='জন্ম নিবন্ধন')),
                ('father_nid_file', models.FileField(blank=True, null=True, upload_to='documents/father-nid/', verbose_name='পিতার এন.আই.ডি')),
                ('mother_nid_file', models.FileField(blank=True, null=True, upload_to='documents/mother-nid/', verbose_name='মাতার এন.আই.ডি')),
                ('student_photo', models.ImageField(upload_to='photos/student-admission-photo/', verbose_name='শিক্ষার্থীর ছবি (ব্যাকগ্রাউন্ডের কালার সাদা)')),
            ],
            options={
                'verbose_name_plural': 'ভর্তির আবেদন ফরম',
                'ordering': ['-id'],
            },
        ),
    ]
