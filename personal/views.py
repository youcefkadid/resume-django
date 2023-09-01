from django.shortcuts import render
from  .models import Aboutp ,Experience,Education,Skills,Portfolio


# Create your views here.



def main(request):
    
    abouts=Aboutp.objects.all()

    return render(request ,'main.html',{'abouts':abouts})



def about(request):
    

    abouts=Aboutp.objects.all()
    
    return render(request ,'about.html' ,{'abouts':abouts })



def experience(request):
    experiences=Experience.objects.all()
    abouts=Aboutp.objects.all()

    return render(request ,'experience.html',{'experiences':experiences,'abouts':abouts},)




def education(request):
    education= Education.objects.all()
    abouts=Aboutp.objects.all()

    return render(request ,'education.html',{'education': education,'abouts':abouts})



def skills(request):
    abouts=Aboutp.objects.all()
    skills= Skills.objects.all()

    return render(request ,'skills.html',{'abouts':abouts ,'skills':skills })


def portfolio(request):
    abouts=Aboutp.objects.all()
    portfolios=Portfolio.objects.all()


    return render(request ,'portfolio.html',{'abouts':abouts,'portfolios':portfolios})



def awards(request):
    abouts=Aboutp.objects.all()

    return render(request ,'awards.html',{'abouts':abouts})




