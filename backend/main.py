"""
SEO Now Tool — FastAPI Backend Entry Point
Author: Marjory D. Marquez | github.com/Marjory00
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import meta, keywords, links, readability, sitemap

# Initialize FastAPI app
app = FastAPI(
    title="SEO Now Tool API",
    description="On-page SEO analysis tool by Marjory D. Marquez.",
    version="1.0.0",
)

# Allow the React frontend dev server to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register each analysis module as its own API route group
app.include_router(meta.router,         prefix="/api/meta",         tags=["Meta Tags"])
app.include_router(keywords.router,     prefix="/api/keywords",     tags=["Keywords"])
app.include_router(links.router,        prefix="/api/links",        tags=["Links"])
app.include_router(readability.router,  prefix="/api/readability",  tags=["Readability"])
app.include_router(sitemap.router,      prefix="/api/sitemap",      tags=["Sitemap"])


@app.get("/")
def root():
    """Health check — confirms the API is running."""
    return {"status": "ok", "message": "SEO Now Tool API is running."}