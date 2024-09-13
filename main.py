from fastapi import FastAPI, Request, Form  # Certifique-se de importar Request aqui
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

# Monta arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configura os diretórios de templates
templates_pages = Jinja2Templates(directory="pages")  # Diretório para o 'trabalhe_conosco.html'
templates_index = Jinja2Templates(directory="pages")  # Diretório para o 'index.html'

class FormData(BaseModel):
    nome: str
    idade: int
    endereco: str
    email: str
    escolaridade: str
    concordo: bool
    trabalho: str
    mensagem: str

# Rota para a página inicial (index.html)
@app.get("/", response_class=HTMLResponse)
def read_index(request: Request):  # Certifique-se de que "request" está presente como parâmetro
    return templates_index.TemplateResponse("index.html", {"request": request})

# Rota para o formulário (trabalhe_conosco.html)
@app.get("/formulario", response_class=HTMLResponse)
def read_form(request: Request):  # Certifique-se de que "request" está presente como parâmetro
    return templates_pages.TemplateResponse("trabalhe_conosco.html", {"request": request})

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