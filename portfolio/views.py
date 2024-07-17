from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Skill, Project, Feedback,Document
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import DocumentForm,FeedbackForm
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib import messages

def home(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

class SkillListView(ListView):
    model = Skill
    template_name = 'skills_list.html'
    context_object_name = 'skills'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['frontend_skills'] = Skill.objects.filter(category='Frontend')
        context['backend_skills'] = Skill.objects.filter(category='Backend')
        context['database_skills'] = Skill.objects.filter(category='Database')
        context['other_skills'] = Skill.objects.exclude(category__in=['Frontend', 'Backend', 'Database'])
        return context

class SkillCreateView(CreateView):
    model = Skill
    template_name = 'skill_form.html'
    fields = ['name', 'category', 'icon']
    def get_success_url(self):
        return reverse_lazy('skills-list')

class SkillUpdateView(UpdateView):
    model = Skill
    template_name = 'skill_form.html'
    fields = ['name', 'category', 'icon']
    def get_success_url(self):
        return reverse_lazy('skills-list')

class SkillDeleteView(DeleteView):
    model = Skill
    template_name = 'skill_confirm_delete.html'
    success_url = reverse_lazy('skills-list')


class ProjectListView(ListView):
    model = Project
    template_name = 'projects.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = self.get_queryset()
        context['django_projects'] = projects.filter(technologies__icontains='Django')
        context['html_projects'] = projects.filter(technologies='HTML')
        context['css_projects'] = projects.filter(technologies='CSS')
        context['javascript_projects'] = projects.filter(technologies__icontains='JavaScript')
        context['react_projects'] = projects.filter(technologies__icontains='React')
        context['nodejs_projects'] = projects.filter(technologies__icontains='Node.js')
        return context
    def get_queryset(self):
        return Project.objects.all()
class ProjectCreateView(CreateView):
    model = Project
    template_name = 'project_form.html'
    fields = ['name', 'image', 'description', 'link']
    def get_success_url(self):
        return reverse_lazy('projects-list')

class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'project_form.html'
    fields = ['name', 'image', 'description', 'link']
    success_url = reverse_lazy('projects-list')

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project_confirm_delete.html'
    success_url = reverse_lazy('projects-list')


def resume_view(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resume')
    else:
        form = DocumentForm()
    
    documents = Document.objects.all()
    return render(request, 'resume.html', {'form': form, 'documents': documents})

def delete_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    if request.method == 'POST':
        document.delete()
        return redirect('resume')
    return render(request, 'resume_confirm_delete.html', {'document': document})


def contact_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save()
            try:
                send_mail(
                    'New Feedback from {}'.format(feedback.name),
                    feedback.message,
                    feedback.email,
                    ['nitishkamisetti123@gmail.com'],  
                    fail_silently=False,
                )
                messages.success(request, 'Your feedback has been submitted successfully!')
            except Exception as e:
                messages.error(request, 'There was an error sending your feedback. Please try again later.')
            return redirect('contact')
        else:
            messages.error(request, 'There was an error with your submission. Please check the form and try again.')
    else:
        form = FeedbackForm()

    return render(request, 'contact.html', {'form': form})