from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter(prefix="/ingredients", tags=["ingredients"])

@router.get("/", response_model=list[schemas.Ingredient])
def read_ingredients(db: Session = Depends(database.get_db)):
    return crud.get_ingredients(db)

@router.post("/", response_model=schemas.Ingredient)
def create_ingredient(ingredient: schemas.IngredientCreate, db: Session = Depends(database.get_db)):
    return crud.create_ingredient(db, ingredient)
