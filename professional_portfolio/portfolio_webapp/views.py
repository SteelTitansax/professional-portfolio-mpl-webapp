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

def cloud_scripting(request):
    sections = {
        "portfolios": load_json("portfolios"),
        "curriculum": load_json("curriculum"),
        "education": load_json("education"),
        "cloudScriptingExperience": load_json("cloudScriptingExperience"),
        "cloudScriptingSkills": load_json("cloudScriptingSkills"),
        "cloudScriptingProjects": load_json("cloudScriptingProjects")       
    }
    return render(request, "cloud_scripting.html", {"sections": sections})   

def selenium(request):
    sections = {
        "portfolios": load_json("portfolios"),
        "curriculum": load_json("curriculum"),
        "education": load_json("education"),
        "seleniumExperience": load_json("seleniumExperience"),
        "seleniumSkills": load_json("seleniumSkills"),
        "seleniumProjects": load_json("seleniumProjects")       
    }
    return render(request, "selenium.html", {"sections": sections})   

def powerautomate(request):
    sections = {
        "portfolios": load_json("portfolios"),
        "curriculum": load_json("curriculum"),
        "education": load_json("education"),
        "powerautomateExperience": load_json("powerautomateExperience"),
        "powerautomateSkills": load_json("powerautomateSkills"),
        "powerautomateProjects": load_json("powerautomateProjects")       
    }
    return render(request, "powerautomate.html", {"sections": sections})   

def uipath(request):
    sections = {
        "portfolios": load_json("portfolios"),
        "curriculum": load_json("curriculum"),
        "education": load_json("education"),
        "uipathExperience": load_json("uipathExperience"),
        "uipathSkills": load_json("uipathSkills"),
        "uipathProjects": load_json("uipathProjects")       
    }
    return render(request, "uipath.html", {"sections": sections})   

def virtual_agents(request):
    sections = {
        "portfolios": load_json("portfolios"),
        "curriculum": load_json("curriculum"),
        "education": load_json("education"),
        "virtualAgentsExperience": load_json("virtualAgentsExperience"),
        "virtualAgentsSkills": load_json("virtualAgentsSkills"),
        "virtualAgentsProjects": load_json("virtualAgentsProjects")       
    }
    return render(request, "virtual_agents.html", {"sections": sections})   

def powerautomate_desktop(request):
    sections = {
        "portfolios": load_json("portfolios"),
        "curriculum": load_json("curriculum"),
        "education": load_json("education"),
        "powerautomateDesktopExperience": load_json("powerautomateDesktopExperience"),
        "powerautomateDesktopSkills": load_json("powerautomateDesktopSkills"),
        "powerautomateDesktopProjects": load_json("powerautomateDesktopProjects")       
    }
    return render(request, "powerautomate_desktop.html", {"sections": sections})   


def machinelearning_portfolio(request):
    sections = {
        "portfolios": load_json("portfolios"),
        "curriculum": load_json("curriculum"),
        "education": load_json("education"),
        "machinelearningExperience": load_json("machinelearningExperience"),
        "machinelearningSkills": load_json("machinelearningSkills"),
        "machinelearningProjects": load_json("machinelearningProjects")       
    }
    return render(request, "machinelearning_portfolio.html", {"sections": sections})   

def supervisedlearning(request):
    sections = {
        "portfolios": load_json("portfolios"),
        "curriculum": load_json("curriculum"),
        "education": load_json("education"),
        "supervisedlearningExperience": load_json("supervisedlearningExperience"),
        "supervisedlearningSkills": load_json("supervisedlearningSkills"),
        "supervisedlearningProjects": load_json("supervisedlearningProjects")       
    }
    return render(request, "supervisedlearning.html", {"sections": sections})   

def unsupervisedlearning(request):
    sections = {
        "portfolios": load_json("portfolios"),
        "curriculum": load_json("curriculum"),
        "education": load_json("education"),
        "unsupervisedlearningExperience": load_json("unsupervisedlearningExperience"),
        "unsupervisedlearningSkills": load_json("unsupervisedlearningSkills"),
        "unsupervisedlearningProjects": load_json("unsupervisedlearningProjects")       
    }
    return render(request, "unsupervisedlearning.html", {"sections": sections})   


def industry40_portfolio(request):
    sections = {
        "portfolios": load_json("portfolios"),
        "curriculum": load_json("curriculum"),
        "education": load_json("education"),
        "industry40Experience": load_json("industry40Experience"),
        "industry40Skills": load_json("industry40Skills"),
        "industry40Projects": load_json("industry40Projects")       
    }
    return render(request, "industry40.html", {"sections": sections})   



def industrialapplications(request):
    sections = {
        "portfolios": load_json("portfolios"),
        "curriculum": load_json("curriculum"),
        "education": load_json("education"),
        "industrialapplicationsExperience": load_json("industrialapplicationsExperience"),
        "industrialapplicationsSkills": load_json("industrialapplicationsSkills"),
        "industrialapplicationsProjects": load_json("industrialapplicationsProjects")       
    }
    return render(request, "industrialapplications.html", {"sections": sections})   