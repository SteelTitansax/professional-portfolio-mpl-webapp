from django.shortcuts import render
import json

def load_json(nombre_archivo):
    with open(f"data/{nombre_archivo}.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)

def home(request):
    sections = {
        "portfolios": load_json("portfolios"),
        "curriculum": load_json("curriculum"),
        "education": load_json("education"),
        "experiences": load_json("experiences"),
        "hobbies": load_json("hobbies"),
        "skills": load_json("skills")
    }

    return render(request, "home.html", {"sections": sections})

def contact(request):
    sections = {
        "portfolios": load_json("portfolios"),
        "curriculum": load_json("curriculum"),
        "education": load_json("education"),
        "experiences": load_json("experiences"),
        "hobbies": load_json("hobbies"),
        "skills": load_json("skills")
    }
    return render(request, "contact.html", {"sections": sections})

def fullstack_portfolio(request):
    sections = {
        "portfolios": load_json("portfolios"),
        "curriculum": load_json("curriculum"),
        "education": load_json("education"),
        "fullstackExperience": load_json("fullstackExperience"),
        "fullstackSkills": load_json("fullstackSkills"),
        "fullstackProjects": load_json("fullstackProjects")       
    }
    return render(request, "fullstack_portfolio.html", {"sections": sections})

def react(request):
    sections = {
        "portfolios": load_json("portfolios"),
        "curriculum": load_json("curriculum"),
        "education": load_json("education"),
        "reactExperience": load_json("reactExperience"),
        "reactSkills": load_json("reactSkills"),
        "reactProjects": load_json("reactProjects")       
    }
    return render(request, "react.html", {"sections": sections})

def angular(request):
    sections = {
        "portfolios": load_json("portfolios"),
        "curriculum": load_json("curriculum"),
        "education": load_json("education"),
        "angularExperience": load_json("angularExperience"),
        "angularSkills": load_json("angularSkills"),
        "angularProjects": load_json("angularProjects")       
    }
    return render(request, "angular.html", {"sections": sections})

def node(request): 
    sections = {
        "portfolios": load_json("portfolios"),
        "curriculum": load_json("curriculum"),
        "education": load_json("education"),
        "nodeExperience": load_json("nodeExperience"),
        "nodeSkills": load_json("nodeSkills"),
        "nodeProjects": load_json("nodeProjects")       
    }
    return render(request, "node.html", {"sections": sections})

def djangoFlask(request):
    sections = {
        "portfolios": load_json("portfolios"),
        "curriculum": load_json("curriculum"),
        "education": load_json("education"),
        "djangoFlaskExperience": load_json("djangoFlaskExperience"),
        "djangoFlaskSkills": load_json("djangoFlaskSkills"),
        "djangoFlaskProjects": load_json("djangoFlaskProjects")       
    }
    return render(request, "djangoFlask.html", {"sections": sections})


def powerApps(request):
    sections = {
        "portfolios": load_json("portfolios"),
        "curriculum": load_json("curriculum"),
        "education": load_json("education"),
        "powerAppsExperience": load_json("powerAppsExperience"),
        "powerAppsSkills": load_json("powerAppsSkills"),
        "powerAppsProjects": load_json("powerAppsProjects")       
    }
    return render(request, "powerApps.html", {"sections": sections})   
def csharp(request):
    sections = {
        "portfolios": load_json("portfolios"),
        "curriculum": load_json("curriculum"),
        "education": load_json("education"),
        "csharpExperience": load_json("csharpExperience"),
        "csharpSkills": load_json("csharpSkills"),
        "csharpProjects": load_json("csharpProjects")       
    }
    return render(request, "csharp.html", {"sections": sections})

def rpa_portfolio(request):
    sections = {
        "portfolios": load_json("portfolios"),
        "curriculum": load_json("curriculum"),
        "education": load_json("education"),
        "rpaExperience": load_json("rpaExperience"),
        "rpaSkills": load_json("rpaSkills"),
        "rpaProjects": load_json("rpaProjects")       
    }
    return render(request, "rpa_portfolio.html", {"sections": sections})   