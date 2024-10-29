from typing import Any
from django.shortcuts import render,redirect 
from django.views.generic import TemplateView 
from .models import Qoutes,Gallary,Slider,Contact,Notice,SchoolInfo,Teacher
from .forms import ComplainForm,StudentAdmissionForm 
from django.contrib import messages 
from django.views.generic.edit import FormView

# Create your views here. 
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qoutes'] = Qoutes.objects.all() 
        context['slider'] = Slider.objects.all()
        context['form'] = ComplainForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ComplainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path_info)
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)
    
    
class AboutView(TemplateView):
    template_name = 'about.html' 
    
    
    
class NoticeView(TemplateView): 
    template_name = 'notice.html'  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notices'] = Notice.objects.all() 
        return context
    
    
class ContactView(TemplateView):
    template_name = 'contact.html' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.all() 
        context['form'] = ComplainForm()
        return context 
    
    def post(self, request, *args, **kwargs):
        form = ComplainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path_info)  # Redirect back to the same page
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)
    
class AdmissionView(FormView):
    template_name = 'admission.html'
    form_class = StudentAdmissionForm

    def form_valid(self, form):
        print("Form Data:", form.cleaned_data)
        form.save()
        messages.success(self.request, 'আপনার আবেদন সফলভাবে জমা হয়েছে!')  # Success message
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form Errors:", form.errors)
        return super().form_invalid(form)

    def get_success_url(self):
        return self.request.path


class AcadamicsView(TemplateView): 
    template_name = 'acadamics.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_info = SchoolInfo.objects.first() 
        context['school_info'] = school_info
        return context
    

class  TeachersView(TemplateView): 
    template_name = 'teacher.html' 
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs) 
        context['teachers'] = Teacher.objects.all().order_by('-id') 
        return context 
    
    
class StuentsView(TemplateView): 
    template_name = 'student.html' 
    

class GallaryView(TemplateView): 
    template_name = 'gallary.html' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallary'] = Gallary.objects.all()
        return context
    
class ResultView(TemplateView): 
    template_name = 'result.html'
    