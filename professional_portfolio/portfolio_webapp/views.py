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