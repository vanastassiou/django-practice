from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:question_id>/', views.detail, name="detail"), # <> captures parts of the requested URL and sends it as keyword arg to specified view function
    path('<int:question_id>/results', views.results, name="results"), # :question_id is the variable name associated with the kwarg
    path('<int:question_id>/vote', views.vote, name="vote") # int: converter determines what patterns should match this part of URL path https://docs.djangoproject.com/en/2.2/_modules/django/urls/converters/
]

# When a URL is requested, Django:
# 1. Loads Python module pointed to by ROOT_URLCONF (default: yourprojectname.urls)
# 2. Finds urlpatterns variable, parses patterns in order, and processes request using first match
# 3. Removes text that matches urlpattern
# 4. Sends remaining text in requested URL to polls.urls (because of include)
# 5. Parses urlpatterns in order until a match
# 6. Captures the value of the matching path pattern and sends it to the polls.view function, labelled with the argument name