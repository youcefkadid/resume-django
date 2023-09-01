from django.urls import path 
from django.views.generic import TemplateView


from . import views


urlpatterns=[

    
path('', views.about , name='about'),
path('experience', views.experience, name='experience'),
path('education', views.education, name='education'),
path('skills', views.skills, name='skills'),
path('portfolio', views.portfolio, name='portfolio'),
path('awards', views.awards, name='awards'),
path('robots.txt', TemplateView.as_view(
        template_name="robots.txt", content_type='text/plain')),





]