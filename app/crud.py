from sqlalchemy.orm import Session
from . import models, schemas

# Recipe CRUD
def get_recipes(db: Session):
    return db.query(models.Recipe).all()

def create_recipe(db: Session, recipe: schemas.RecipeCreate):
    db_recipe = models.Recipe(**recipe.dict())
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

# Ingredient CRUD
def get_ingredients(db: Session):
    return db.query(models.Ingredient).all()

def create_ingredient(db: Session, ingredient: schemas.IngredientCreate):
    db_ingredient = models.Ingredient(**ingredient.dict())
    db.add(db_ingredient)
    db.commit()
    db.refresh(db_ingredient)
    return db_ingredient
