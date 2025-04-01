from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI(title="IITM Assignment API (Vercel Proxy)")

# 👇 Your backend hosted on Render
EXTERNAL_API_BASE = "https://tds-solver-9qv3.onrender.com"

# Allow CORS for frontend use
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔁 Proxy for /api/
@app.post("/api/")
async def proxy_api(request: Request):
    form = await request.form()
    files = {}
    data = {}

    for key, value in form.multi_items():
        if isinstance(value, UploadFile):
            files[key] = (value.filename, await value.read(), value.content_type)
        else:
            data[key] = value

    async with httpx.AsyncClient() as client:
        resp = await client.post(
            f"{EXTERNAL_API_BASE}/api/",
            data=data,
            files=files
        )
    return resp.json()

# 🔁 Proxy for /debug/{function_name}
@app.post("/debug/{function_name}")
async def proxy_debug(request: Request, function_name: str):
    form = await request.form()
    files = {}
    data = {}

    for key, value in form.multi_items():
        if isinstance(value, UploadFile):
            files[key] = (value.filename, await value.read(), value.content_type)
        else:
            data[key] = value

    async with httpx.AsyncClient() as client:
        resp = await client.post(
            f"{EXTERNAL_API_BASE}/debug/{function_name}",
            data=data,
            files=files
        )
    return resp.json()

# Health check
@app.get("/")
def home():
    return {"message": "Vercel proxy is live and forwarding to Render!"}