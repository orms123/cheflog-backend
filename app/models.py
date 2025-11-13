from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# Recipe table
class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    instructions = Column(String)
    cost_per_portion = Column(Float)
    ingredients = relationship("Ingredient", back_populates="recipe")
    prep_lists = relationship("PrepTask", back_populates="recipe")

# Ingredient table
class Ingredient(Base):
    __tablename__ = "ingredients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    quantity = Column(Float)
    unit = Column(String)
    cost_per_unit = Column(Float)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    recipe = relationship("Recipe", back_populates="ingredients")

# Prep list stub
class PrepTask(Base):
    __tablename__ = "prep_tasks"
    id = Column(Integer, primary_key=True, index=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    quantity = Column(Float)
    status = Column(String, default="pending")
    recipe = relationship("Recipe", back_populates="prep_lists")

# Health & Safety stub
class Checklist(Base):
    __tablename__ = "checklists"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)  # opening, closing, fridge, cleaning
    date = Column(String)
    created_by = Column(String)

class ChecklistItem(Base):
    __tablename__ = "checklist_items"
    id = Column(Integer, primary_key=True, index=True)
    checklist_id = Column(Integer, ForeignKey("checklists.id"))
    name = Column(String)
    completed = Column(String, default="no")
    timestamp = Column(String, nullable=True)
    signed_by = Column(String, nullable=True)
