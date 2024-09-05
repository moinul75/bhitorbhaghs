from django.db import models

# Create your models here.   
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        abstract = True 
        
class SocialMedia(TimeStampedModel):
    facebook = models.URLField(max_length=500, blank=True, null=True)
    twitter = models.URLField(max_length=500, blank=True, null=True)
    youtube = models.URLField(max_length=500, blank=True, null=True)
    linkedin = models.URLField(max_length=500, blank=True, null=True)
    instagram = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self) -> str:
        return f"Social Media Links"

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "সামাজিক যোগাযোগ মাধ্যম"

class Icon(TimeStampedModel):
    name = models.CharField(max_length=50,null=True)  # e.g., 'fa-map-marker-alt', 'fa-envelope-open', etc.
    class_name = models.CharField(max_length=50,null=True)  # Font Awesome class, e.g., 'fa-map-marker-alt'

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Icon"


class Contact(TimeStampedModel): 
    location = models.CharField(max_length=255, blank=True, null=True) 
    email = models.EmailField(max_length=255, null=True, blank=True, unique=True) 
    phone = models.CharField(max_length=20, null=True, blank=True)  
    map_link = models.URLField(max_length=500, blank=True, null=True) 
    icons = models.ManyToManyField(Icon, blank=True)

    def __str__(self) -> str:
        return f"{self.location} -> {self.email} -> {self.phone}" 
    
    class Meta:  
        ordering = ['-id']
        verbose_name_plural = "যোগাযোগ"
    
    
class Complain(models.Model):
    gurdian_name = models.CharField(max_length=100)
    gurdian_email = models.EmailField()
    student_name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return f"Complaint from {self.gurdian_name} about {self.student_name}"

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Complain" 
        
class ImportantLink(models.Model):
    link_name = models.CharField(max_length=100,verbose_name="লিঙ্ক Name")
    link = models.URLField(max_length=500,verbose_name="লিঙ্ক")

    def __str__(self) -> str:
        return f"{self.link_name}: {self.link}"

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "গুরুত্বপূর্ণ লিঙ্ক" 
        
    

class Slider(models.Model): 
    name = models.CharField(max_length=25,null=True,blank=True) 
    slide_img = models.ImageField(upload_to='Sliders/',null=True,blank=True) 
    
    def __str__(self):
        return self.name  
    
class Qoutes(models.Model):
    image = models.ImageField(upload_to='Quote/', null=True, blank=True)
    writer_name = models.CharField(max_length=100)
    quote = models.TextField()

    def __str__(self) -> str:
        return f"{self.writer_name}: {self.quote[:50]}..."

    class Meta:
        ordering = ['writer_name']
        verbose_name_plural = "অনুপ্রেরণামূলক উক্তি সমগ্র" 
        
        
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Teachers/', blank=True, null=True)
    facebook = models.URLField(max_length=500, blank=True, null=True)
    instagram = models.URLField(max_length=500, blank=True, null=True)
    linkedin = models.URLField(max_length=500, blank=True, null=True)
    twitter = models.URLField(max_length=500, blank=True, null=True)
    youtube = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.designation}"

    class Meta:
        ordering = ['name']
        verbose_name_plural = "শিক্ষকবৃন্দ"
    
    
class Gallary(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='Gallery/') 
    created_at = models.DateTimeField(auto_now_add=True,null=True) 
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Gallary"  



#notice Section 
class Notice(TimeStampedModel): 
    title = models.TextField(verbose_name="শিরোনাম") 
    attachment = models.FileField(upload_to='Notice/',null=True,blank=True,verbose_name="নোটিশ তথ্য PDF") 
    
    def __str__(self) -> str:
        return f"{self.title} -> {self.created_at}" 
    
    class Meta: 
        ordering = ['-id'] 
        verbose_name_plural = 'নোটিশ বোর্ড' 
        
               
class ExamResult(models.Model):
    exam_name = models.CharField(max_length=255, verbose_name="পরীক্ষার নাম")  
    year = models.IntegerField(verbose_name="সাল")  # Year
    total_students = models.PositiveIntegerField(verbose_name="মোট পরীক্ষার্থী")  

    # Passing students (boys and girls)
    passing_students_boys = models.PositiveIntegerField(verbose_name="পাসকৃত শিক্ষার্থী (Boys)")  
    passing_students_girls = models.PositiveIntegerField(verbose_name="পাসকৃত শিক্ষার্থী (Girls)")

    # GPA 5.00 students (boys and girls)
    gpa_5_boys = models.PositiveIntegerField(verbose_name="জিপিএ ৫.০০ (Boys)")  
    gpa_5_girls = models.PositiveIntegerField(verbose_name="জিপিএ ৫.০০ (Girls)")  

    pass_rate = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="পাসের হার")  

    class Meta:
        ordering = ['-year']  
        verbose_name_plural = "Exam Result"  

    def __str__(self):
        return f"{self.exam_name} - {self.year}"  
    
    
class SchoolInfo(models.Model):
    eiin = models.CharField(max_length=15, verbose_name="বিদ্যালয়ের EIIN")  
    school_name_bn = models.CharField(max_length=255, verbose_name="বিদ্যালয়ের নাম") 
    school_name_en = models.CharField(max_length=255, verbose_name="SCHOOL NAME")  
    address = models.TextField(verbose_name="গ্রাম/বাড়ী ও সড়কের বিবরণ") 
    ward_number = models.CharField(max_length=10, verbose_name="ওয়ার্ড নম্বর", blank=True, null=True) 
    post_office = models.CharField(max_length=100, verbose_name="পোস্ট অফিস")  
    police_station = models.CharField(max_length=100, verbose_name="পুলিশ স্টেশন")  
    district = models.CharField(max_length=100, verbose_name="জেলা") 
    mobile = models.CharField(max_length=20, verbose_name="মোবাইল", blank=True, null=True)
    website = models.URLField(verbose_name="Website", blank=True, null=True)
    school_shift = models.CharField(max_length=50, verbose_name="বিদ্যালয়ের শিফট", blank=True, null=True) 
    class_operations = models.CharField(max_length=100, verbose_name="শ্রেণি কার্যক্রম", blank=True, null=True) 
    total_land_area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="মোট জমির পরিমান (একর)", blank=True, null=True) 
    total_classrooms = models.PositiveIntegerField(verbose_name="মোট শ্রেণিকক্ষ সংখ্যা", blank=True, null=True) 
    ict_lab_count = models.PositiveIntegerField(verbose_name="আইসিটি ল্যাব সংখ্যা", blank=True, null=True)
    library_room_count = models.PositiveIntegerField(verbose_name="পাঠাগার এর জন্য কক্ষ সংখ্যা", blank=True, null=True)  
    has_boundary_wall = models.BooleanField(verbose_name="সীমানা প্রাচীর আছে কি না", default=False)  
    has_playground = models.BooleanField(verbose_name="খেলার মাঠ আছে কি না", default=False)  
    union_or_municipality = models.CharField(max_length=100, verbose_name="ইউনিয়ন/পৌরসভা/সিটি কর্পোরেশন", blank=True, null=True)  
    postal_code = models.CharField(max_length=10, verbose_name="পোস্ট কোড", blank=True, null=True)  
    upazila = models.CharField(max_length=100, verbose_name="উপজেলা", blank=True, null=True)  
    division = models.CharField(max_length=100, verbose_name="বিভাগ") 
    email = models.EmailField(verbose_name="E-Mail", blank=True, null=True)  
    total_students = models.PositiveIntegerField(verbose_name="শিক্ষার্থীর সংখ্যা", blank=True, null=True)  
    school_type = models.CharField(max_length=100, verbose_name="বিদ্যালয়ের ধরণ", blank=True, null=True) 
    building_count = models.PositiveIntegerField(verbose_name="ভবন সংখ্যা", blank=True, null=True)  
    multimedia_classroom_count = models.PositiveIntegerField(verbose_name="মাল্টিমিডিয়া শ্রেণিকক্ষ সংখ্যা", blank=True, null=True)  
    science_lab_room_count = models.PositiveIntegerField(verbose_name="বিজ্ঞানাগার এর জন্য কক্ষ সংখ্যা", blank=True, null=True)  
    has_auditorium = models.BooleanField(verbose_name="অডিটোরিয়াম আছে কি না", default=False)  

    class Meta:
        verbose_name_plural = "এক নজরে বিদ্যালয়ের পরিচিতি"
        ordering = ['-id'] 

    def __str__(self):
        return self.eiin 
    
    
class ClassInfo(models.Model):
    CLASS_CHOICES = [
        ('Six', 'Six'),
        ('Seven', 'Seven'),
        ('Eight', 'Eight'),
        ('Nine', 'Nine'),
        ('Ten', 'Ten'),
    ]

    SHIFT_CHOICES = [
        ('Morning', 'Morning'),
        ('Day', 'Day'),
        ('Evening', 'Evening'),
    ]

    SECTION_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    ]

    # Basic info
    student_class = models.CharField(max_length=20, choices=CLASS_CHOICES, verbose_name="শ্রেণি") 
    shift = models.CharField(max_length=20, choices=SHIFT_CHOICES, verbose_name="শিফট")  
    section = models.CharField(max_length=5, choices=SECTION_CHOICES, verbose_name="সেকশন", blank=True, null=True) 
    total_students = models.PositiveIntegerField(verbose_name="মোট শিক্ষার্থী সংখ্যা")  
    # Gender-based student info
    boys = models.PositiveIntegerField(verbose_name="ছেলে শিক্ষার্থী সংখ্যা")  
    girls = models.PositiveIntegerField(verbose_name="মেয়ে শিক্ষার্থী সংখ্যা")  

    # Religion-based student info
    muslim_students = models.PositiveIntegerField(verbose_name="মুসলিম শিক্ষার্থী সংখ্যা")  
    hindu_students = models.PositiveIntegerField(verbose_name="হিন্দু শিক্ষার্থী সংখ্যা")  
    buddhist_students = models.PositiveIntegerField(verbose_name="বৌদ্ধ শিক্ষার্থী সংখ্যা", blank=True, null=True)  
    christian_students = models.PositiveIntegerField(verbose_name="খ্রিস্টান শিক্ষার্থী সংখ্যা", blank=True, null=True) 

    # Group-based student info
    science_students = models.PositiveIntegerField(verbose_name="বিজ্ঞান বিভাগে শিক্ষার্থী সংখ্যা", blank=True, null=True) 
    commerce_students = models.PositiveIntegerField(verbose_name="ব্যবসা শিক্ষা বিভাগে শিক্ষার্থী সংখ্যা", blank=True, null=True)  
    humanities_students = models.PositiveIntegerField(verbose_name="মানবিক বিভাগে শিক্ষার্থী সংখ্যা", blank=True, null=True)  

    # Freedom fighter-related student info
    freedom_fighter_children = models.PositiveIntegerField(verbose_name="মুক্তিযোদ্ধার সন্তান শিক্ষার্থী সংখ্যা", blank=True, null=True)  
    freedom_fighter_grandchildren = models.PositiveIntegerField(verbose_name="মুক্তিযোদ্ধার স.সন্তান শিক্ষার্থী সংখ্যা", blank=True, null=True)  

    # Disability info
    disabled_students_total = models.PositiveIntegerField(verbose_name="মোট প্রতিবন্ধি শিক্ষার্থী সংখ্যা", blank=True, null=True)  
    autistic_students = models.PositiveIntegerField(verbose_name="অটিস্টিক শিক্ষার্থী সংখ্যা", blank=True, null=True)  
    physically_disabled_students = models.PositiveIntegerField(verbose_name="শারীরিক প্রতিবন্ধি শিক্ষার্থী সংখ্যা", blank=True, null=True)  

    class Meta:
        verbose_name_plural = "এক নজরে শ্রেণির তথ্য"
        ordering = ['student_class', 'shift', 'section']  

    def __str__(self):
        return f"{self.student_class} - {self.shift} - {self.section or 'N/A'}" 
    
    
class StudentAdmission(models.Model):
    # Student info
    student_name_bn = models.CharField(max_length=255, verbose_name="শিক্ষার্থীর নাম (বাংলায়)")
    student_name_en = models.CharField(max_length=255, verbose_name="শিক্ষার্থীর নাম (ইংরেজি)")
    
    # Father's info
    father_name_bn = models.CharField(max_length=255, verbose_name="পিতার নাম (বাংলায়)")
    father_name_en = models.CharField(max_length=255, verbose_name="পিতার নাম (ইংরেজি)")
    father_nid = models.CharField(max_length=17, verbose_name="পিতার জাতীয় পরিচয় পত্র নং", blank=True, null=True)
    
    # Mother's info
    mother_name_bn = models.CharField(max_length=255, verbose_name="মাতার নাম (বাংলায়)")
    mother_name_en = models.CharField(max_length=255, verbose_name="মাতার নাম (ইংরেজি)")
    mother_nid = models.CharField(max_length=17, verbose_name="মাতার জাতীয় পরিচয় পত্র নং", blank=True, null=True)
    
    # Address info
    permanent_address = models.TextField(verbose_name="স্থায়ী ঠিকানা")
    present_address = models.TextField(verbose_name="বর্তমান ঠিকানা")
    
    # Parent's income
    annual_income = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="পিতা/মাতার বাৎসরিক আয়", blank=True, null=True)
    
    # Guardian contact info
    guardian_mobile = models.CharField(max_length=15, verbose_name="অভিভাবকের মোবাইল নম্বার (ইংরেজি)")
    guardian_occupation = models.CharField(max_length=255, verbose_name="পেশা", blank=True, null=True)
    guardian_name = models.CharField(max_length=255, verbose_name="পিতা মাতার অবর্তমানে বৈধ অভিভাবকের নাম", blank=True, null=True)
    guardian_address = models.TextField(verbose_name="ঠিকানা", blank=True, null=True)
    
    # Other info
    nationality = models.CharField(max_length=50, verbose_name="জাতীয়তা", default="বাংলাদেশী")
    religion = models.CharField(max_length=50, verbose_name="ধর্ম")
    birth_date = models.DateField(verbose_name="জন্ম তারিখ (mm/dd/yyyy)")
    age = models.IntegerField(verbose_name="বয়স")
    birth_registration_no = models.CharField(max_length=17, verbose_name="জাতীয় জন্ম নিবন্ধন নম্বার", blank=True, null=True)
    
    # Previous school info
    previous_school_name = models.CharField(max_length=255, verbose_name="পূর্বে যে বিদ্যালয়ে ছাত্র/ছাত্রী ছিল তাহার নাম", blank=True, null=True)
    previous_class = models.CharField(max_length=50, verbose_name="যে শ্রেণীতে অধ্যায়নরত ছিল", blank=True, null=True)
    last_exam_passed = models.CharField(max_length=255, verbose_name="শেষ যে পরীক্ষায় উত্তীর্ণ হয়েছে তার নাম", blank=True, null=True)
    result_gpa = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="রেজাল্ট(জি.পি.এ)", blank=True, null=True)
    
    # Admission info
    admission_class = models.CharField(max_length=50, verbose_name="যে শ্রেণীতে ভর্তি হতে ইচ্ছুক")
    transfer_certificate_no = models.CharField(max_length=50, verbose_name="ছাড়পত্র নং", blank=True, null=True)
    
    # Additional info
    student_job = models.CharField(max_length=255, verbose_name="ছাত্র/ছাত্রী কোন পেশায় জড়িত থাকলে পেশার নাম", blank=True, null=True)
    quota = models.CharField(max_length=50, verbose_name="কোটা", blank=True, null=True)
    
    # File uploads
    birth_certificate = models.FileField(upload_to='documents/birth-certificate/', verbose_name="জন্ম নিবন্ধন", blank=True, null=True)
    father_nid_file = models.FileField(upload_to='documents/father-nid/', verbose_name="পিতার এন.আই.ডি", blank=True, null=True)
    mother_nid_file = models.FileField(upload_to='documents/mother-nid/', verbose_name="মাতার এন.আই.ডি", blank=True, null=True)
    student_photo = models.ImageField(upload_to='photos/student-admission-photo/', verbose_name="শিক্ষার্থীর ছবি (ব্যাকগ্রাউন্ডের কালার সাদা)")

    def __str__(self):
        return f"{self.student_name_bn} - {self.student_name_en}" 
    
    
    class Meta:
        verbose_name_plural = "ভর্তির আবেদন ফরম"
        ordering = ['-id'] 