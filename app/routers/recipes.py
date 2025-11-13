from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter(prefix="/recipes", tags=["recipes"])

@router.get("/", response_model=list[schemas.Recipe])
def read_recipes(db: Session = Depends(database.get_db)):
    return crud.get_recipes(db)

@router.post("/", response_model=schemas.Recipe)
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(database.get_db)):
    return crud.create_recipe(db, recipe)
