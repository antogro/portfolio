from django.shortcuts import render
from .models import Project


# Create your views here.
def project_list(request):
    """
    affiche la liste des projets
    :param request: HttpRequest
    """
    # This function handles the request to display the list of projects.
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects}
                  )


def project_detail(request, project_id):
    """
    affiche le détail d'un projet
    :param request: HttpRequest
    :param project_id: int
    """
    # This function handles the request to display the details of a specific project.
    project = Project.objects.get(id=project_id)
    return render(request, 'projects/project_detail.html', {'project': project}
                  )
