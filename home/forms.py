from django import forms
from .models import Complain,StudentAdmission

class ComplainForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = ['gurdian_name', 'gurdian_email', 'student_name', 'class_name', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        } 
        
        
class StudentAdmissionForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="জন্ম তারিখ")

    # Example of increasing the size of text fields that might require more space
    permanent_address = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 1, 'placeholder': 'স্থায়ী ঠিকানা লিখুন'}),
        label="স্থায়ী ঠিকানা"
    )
    
    present_address = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 1, 'placeholder': 'বর্তমান ঠিকানা লিখুন'}),
        label="বর্তমান ঠিকানা"
    )
    
    guardian_address = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 1, 'placeholder': 'অভিভাবকের ঠিকানা লিখুন'}),
        label="ঠিকানা"
    )
    
    # You can modify other fields similarly if necessary
    student_job = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 1, 'placeholder': 'পেশার নাম লিখুন'}),
        label="ছাত্র/ছাত্রী কোন পেশায় জড়িত থাকলে পেশার নাম"
    )
    
    # Other fields remain unchanged
    class Meta:
        model = StudentAdmission
        fields = [
            'student_name_bn', 'student_name_en',
            'father_name_bn', 'father_name_en', 'father_nid',
            'mother_name_bn', 'mother_name_en', 'mother_nid',
            'permanent_address', 'present_address', 'annual_income',
            'guardian_mobile', 'guardian_occupation', 'guardian_name', 'guardian_address',
            'nationality', 'religion', 'birth_date', 'age', 'birth_registration_no',
            'previous_school_name', 'previous_class', 'last_exam_passed', 'result_gpa',
            'admission_class', 'transfer_certificate_no', 'student_job', 'quota',
            'birth_certificate', 'father_nid_file', 'mother_nid_file', 'student_photo'
        ]
        labels = {
            'student_name_bn': 'শিক্ষার্থীর নাম (বাংলায়)',
            'student_name_en': 'শিক্ষার্থীর নাম (ইংরেজি)',
            'father_name_bn': 'পিতার নাম (বাংলায়)',
            'father_name_en': 'পিতার নাম (ইংরেজি)',
            'father_nid': 'পিতার জাতীয় পরিচয় পত্র নং',
            'mother_name_bn': 'মাতার নাম (বাংলায়)',
            'mother_name_en': 'মাতার নাম (ইংরেজি)',
            'mother_nid': 'মাতার জাতীয় পরিচয় পত্র নং',
            'permanent_address': 'স্থায়ী ঠিকানা',
            'present_address': 'বর্তমান ঠিকানা',
            'annual_income': 'পিতা/মাতার বাৎসরিক আয়',
            'guardian_mobile': 'অভিভাবকের মোবাইল নম্বার (ইংরেজি)',
            'guardian_occupation': 'পেশা',
            'guardian_name': 'পিতা মাতার অবর্তমানে বৈধ অভিভাবকের নাম',
            'guardian_address': 'ঠিকানা',
            'nationality': 'জাতীয়তা',
            'religion': 'ধর্ম',
            'birth_date': 'জন্ম তারিখ (mm/dd/yyyy)',
            'age': 'বয়স',
            'birth_registration_no': 'জাতীয় জন্ম নিবন্ধন নম্বার',
            'previous_school_name': 'পূর্বে যে বিদ্যালয়ে ছাত্র/ছাত্রী ছিল তাহার নাম',
            'previous_class': 'যে শ্রেণীতে অধ্যায়নরত ছিল',
            'last_exam_passed': 'শেষ যে পরীক্ষায় উত্তীর্ণ হয়েছে তার নাম',
            'result_gpa': 'রেজাল্ট(জি.পি.এ)',
            'admission_class': 'যে শ্রেণীতে ভর্তি হতে ইচ্ছুক',
            'transfer_certificate_no': 'ছাড়পত্র নং',
            'student_job': 'ছাত্র/ছাত্রী কোন পেশায় জড়িত থাকলে পেশার নাম',
            'quota': 'কোটা',
            'birth_certificate': 'জন্ম নিবন্ধন',
            'father_nid_file': 'পিতার এন.আই.ডি',
            'mother_nid_file': 'মাতার এন.আই.ডি',
            'student_photo': 'শিক্ষার্থীর ছবি (ব্যাকগ্রাউন্ডের কালার সাদা)',
        }
