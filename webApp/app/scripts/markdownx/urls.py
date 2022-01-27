from django.urls import path, re_path

from .views import (
    ImageUploadView,
    MarkdownifyView,
)


urlpatterns = [
    re_path(r'^upload/$', ImageUploadView.as_view(), name='markdownx_upload'),
    re_path(r'^markdownify/$', MarkdownifyView.as_view(), name='markdownx_markdownify'),
]