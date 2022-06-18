from django.views.generic import ListView
from projects.models import Project

# Create your views here.


class ProjectListView(ListView):
    model = Project
    template_name = "projects/list.html"
