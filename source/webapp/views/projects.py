from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, RedirectView

from webapp.forms import ProjectForm, ProjectIssueForm
from webapp.models import Project, Issue


class ProjectsView(ListView):
    template_name = 'project/projects_view.html'
    model = Project
    context_object_name = 'projects'


class ProjectsRedirectView(RedirectView):
    pattern_name = 'projects_view'


class ProjectDetailsView(DetailView):
    template_name = 'project/project_details_view.html'
    model = Project


class ProjectAddView(PermissionRequiredMixin, CreateView):
    permission_required = 'webapp.add_project'
    template_name = 'project/project_add_view.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_details_view', kwargs={'pk': self.object.pk})


class ProjectIssueAddView(PermissionRequiredMixin, CreateView):
    permission_required = 'webapp.add_project_issue'
    model = Issue
    template_name = 'project/project_issue_add_view.html'
    form_class = ProjectIssueForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        issue = form.save(commit=False)
        issue.project = project
        issue.save()
        return redirect('project_details_view', pk=project.pk)
