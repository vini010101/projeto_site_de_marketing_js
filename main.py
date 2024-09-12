from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

# Monta arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configura o diretório de templates para a pasta "pages"
templates = Jinja2Templates(directory="pages")

class FormData(BaseModel):
    nome: str
    idade: int
    endereco: str
    email: str
    escolaridade: str
    concordo: bool
    trabalho: str
    mensagem: str

# Renderiza o template HTML correto
@app.get("/", response_class=HTMLResponse)
def read_form(request: Request):
    return templates.TemplateResponse("trabalhe_conosco.html", {"request": request})

# Submissão do formulário
@app.post("/submit")
def submit_form(
    nome: str = Form(...),
    idade: int = Form(...),
    endereco: str = Form(...),
    email: str = Form(...),
    escolaridade: str = Form(...),
    concordo: bool = Form(...),
    trabalho: str = Form(...),
    mensagem: str = Form(...)
):
    return {
        "nome": nome,
        "idade": idade,
        "endereco": endereco,
        "email": email,
        "escolaridade": escolaridade,
        "concordo": concordo,
        "trabalho": trabalho,
        "mensagem": mensagem
    }
