from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from .database import Base

# ---------------------------
# RECIPES
# ---------------------------

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    instructions = Column(Text, nullable=True)
    cost_per_portion = Column(Float, default=0.0)

    # Relationships
    ingredients = relationship("Ingredient", back_populates="recipe", cascade="all, delete-orphan")
    prep_steps = relationship("PrepStep", back_populates="recipe", cascade="all, delete-orphan")
    checklists = relationship("Checklist", back_populates="recipe", cascade="all, delete-orphan")


# ---------------------------
# INGREDIENTS
# ---------------------------

class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    quantity = Column(Float, default=0)
    unit = Column(String, nullable=True)
    cost_per_unit = Column(Float, default=0.0)

    # Foreign key to Recipe
    recipe_id = Column(Integer, ForeignKey("recipes.id"), nullable=False)
    recipe = relationship("Recipe", back_populates="ingredients")


# ---------------------------
# PREP TASKS
# ---------------------------

class PrepTask(Base):
    __tablename__ = "preptasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)

    # Relationship to PrepStep
    prep_steps = relationship("PrepStep", back_populates="task", cascade="all, delete-orphan")


# ---------------------------
# PREP STEPS
# ---------------------------

class PrepStep(Base):
    __tablename__ = "prepsteps"

    id = Column(Integer, primary_key=True, index=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"), nullable=False)
    task_id = Column(Integer, ForeignKey("preptasks.id"), nullable=False)
    quantity_needed = Column(Float, default=0)
    unit = Column(String, nullable=True)
    notes = Column(Text, nullable=True)

    recipe = relationship("Recipe", back_populates="prep_steps")
    task = relationship("PrepTask", back_populates="prep_steps")


# ---------------------------
# CHECKLISTS
# ---------------------------

class Checklist(Base):
    __tablename__ = "checklists"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    recipe_id = Column(Integer, ForeignKey("recipes.id"), nullable=False)
    recipe = relationship("Recipe", back_populates="checklists")

    # Checklist items
    items = relationship("ChecklistItem", back_populates="checklist", cascade="all, delete-orphan")


# ---------------------------
# CHECKLIST ITEMS
# ---------------------------

class ChecklistItem(Base):
    __tablename__ = "checklist_items"

    id = Column(Integer, primary_key=True, index=True)
    checklist_id = Column(Integer, ForeignKey("checklists.id"), nullable=False)
    description = Column(String, nullable=False)
    completed = Column(Boolean, default=False)

    checklist = relationship("Checklist", back_populates="items")
