from django.contrib import admin 
from .models import Slider,Complain,Contact,SocialMedia,Teacher,ImportantLink,Qoutes,Gallary,Icon,ExamResult,Notice,SchoolInfo,ClassInfo,StudentAdmission

# Register your models here. 
admin.site.register(Slider) 
admin.site.register(Complain) 
admin.site.register(Contact)
admin.site.register(SocialMedia)
admin.site.register(Teacher) 
admin.site.register(ImportantLink) 
admin.site.register(Qoutes)  
admin.site.register(Gallary) 
admin.site.register(Icon) 
admin.site.register(ExamResult) 
admin.site.register(Notice)  
admin.site.register(SchoolInfo)  
admin.site.register(StudentAdmission)

@admin.register(ClassInfo)
class ClassInfoAdmin(admin.ModelAdmin):
    list_display = ('student_class', 'shift', 'section', 'total_students', 'boys', 'girls', 'muslim_students', 'hindu_students', 'science_students', 'freedom_fighter_children', 'disabled_students_total', 'autistic_students', 'physically_disabled_students')
    list_filter = ('student_class', 'shift', 'section')
    search_fields = ('student_class', 'shift', 'section')



