from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    name = "Mojtaba"  
    skills = ["Python", "Java", "AWS"]
    return templates.TemplateResponse("portfolio.html", {"request": request, "name": name, "skills": skills})

@app.get("/contact", response_class=HTMLResponse)
def read_contact(request: Request):
    name = "Mojtaba"
    return templates.TemplateResponse("contact.html", {"request": request, "name": name})

@app.post("/contact", response_class=HTMLResponse)
def submit_contact(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...)
):
    # Handle the form data (name, email, message) here, e.g., save to a database
    return templates.TemplateResponse("contact_submission.html", {"request": request, "name": name, "email": email, "message": message})
