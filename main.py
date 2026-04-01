from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from dotenv import load_dotenv
from pathlib import Path
from storyboard_builder import build_storyboard

# Load environment variables from .env
load_dotenv()

# Ensure static/panels/ directory exists unconditionally on startup
panels_dir = Path("static") / "panels"
panels_dir.mkdir(parents=True, exist_ok=True)

app = FastAPI(title="The Pitch Visualizer")

# Mount static files folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure templates
templates = Jinja2Templates(directory="templates")

class GenerateRequest(BaseModel):
    text: str
    style: str

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Serves the front-end template."""
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/generate")
async def generate(payload: GenerateRequest):
    """Endpoint triggered by the frontend to process the narrative and generate panels."""
    panels = build_storyboard(payload.text, payload.style)
    return panels
