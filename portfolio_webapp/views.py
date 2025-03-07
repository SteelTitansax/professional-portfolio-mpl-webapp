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

    print(sections["hobbies"])
    return render(request, "home.html", {"sections": sections})
