"""
AI Photography Coach - Python Package
"""

__version__ = "0.1.0"
__author__ = "Prasad Tilloo"

from src.rag_pipeline import PhotographyKnowledgeBase
from src.photo_analyzer import PhotoAnalyzer

__all__ = [
    "PhotographyKnowledgeBase",
    "PhotoAnalyzer"
]
