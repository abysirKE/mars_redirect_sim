from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("landing.html", {"request": request})

@app.get("/redirect")
def redirect_to_job():
    # Simulate insecure redirect to HTTP
    target_url = "http://example.com/job-alert"
    return RedirectResponse(url=target_url)
