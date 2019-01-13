from django.urls import path
from django.views.generic import TemplateView

# from {{ cookiecutter.project_slug }}.core.views import (
# )

app_name = "core"
urlpatterns = [
     path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
]
