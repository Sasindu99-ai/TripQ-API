from typing import Type

from django.urls import include as django_include
from django.urls import path as django_path

from vvecon.zorion.views import API, View

__all__ = ['paths', 'include']


def paths(view: Type[View] | Type[API], app_name: str = NotImplemented) -> list:
    return view().generateURLPatterns(app_name=app_name)


def include(appUrls: str) -> list:
    return django_path('', django_include(appUrls))
