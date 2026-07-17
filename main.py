from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="SolutAI API",
    description="Professional AI Backend",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this later to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["System"])
async def home():
    return {
        "success": True,
        "application": "SolutAI API",
        "version": "1.0.0",
        "status": "Running",
        "documentation": "/docs"
    }


@app.get("/health", tags=["System"])
async def health():
    return {
        "success": True,
        "status": "healthy",
        "server": "online"
    }


@app.get("/api/info", tags=["System"])
async def api_info():
    return {
        "name": "SolutAI API",
        "version": "1.0.0",
        "developer": "LivingTech",
        "message": "Backend is working successfully."
    }
