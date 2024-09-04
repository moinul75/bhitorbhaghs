from django.shortcuts import render,redirect 
from django.views.generic import TemplateView 
from .models import Qoutes,Gallary,Slider,Contact
from .forms import ComplainForm

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
            return redirect(request.path_info)  # Redirect back to the same page
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)
    
    
class AboutView(TemplateView):
    template_name = 'about.html' 
    
    
    
class NoticeView(TemplateView):
    template_name = 'notice.html' 
    
    
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
    
class AdmissionView(TemplateView):
    template_name = 'admission.html'


class AcadamicsView(TemplateView): 
    template_name = 'acadamics.html' 
    

class  TeachersView(TemplateView): 
    template_name = 'teacher.html' 
    
    
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
    