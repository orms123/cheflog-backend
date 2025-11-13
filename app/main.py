from fastapi import FastAPI
from .database import engine, Base
from .routers import recipes, ingredients

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="ChefLog API")

# Include routers
app.include_router(recipes.router)
app.include_router(ingredients.router)
