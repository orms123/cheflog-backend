from typing import List, Optional
from pydantic import BaseModel

# Ingredient schemas
class IngredientBase(BaseModel):
    name: str
    quantity: Optional[float] = 0
    unit: Optional[str] = None
    cost_per_unit: Optional[float] = 0.0

class IngredientCreate(IngredientBase):
    pass

class Ingredient(IngredientBase):
    id: int
    class Config:
        orm_mode = True

# Recipe schemas
class RecipeBase(BaseModel):
    name: str
    instructions: Optional[str] = None
    cost_per_portion: Optional[float] = 0.0

class RecipeCreate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int
    ingredients: List[Ingredient] = []
    class Config:
        orm_mode = True
