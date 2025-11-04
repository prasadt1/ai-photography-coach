"""
Utility functions for AI Photography Coach
"""

from pathlib import Path
from typing import List, Dict
import os


def get_project_root() -> Path:
    """Get project root directory"""
    return Path(__file__).parent.parent


def ensure_directories_exist():
    """Create necessary directories if they don't exist"""
    dirs = [
        get_project_root() / "data",
        get_project_root() / "data" / "sample_photos",
        get_project_root() / "data" / "vector_stores",
    ]
    
    for dir_path in dirs:
        dir_path.mkdir(parents=True, exist_ok=True)


def load_env_variables():
    """Load environment variables from .env file"""
    from dotenv import load_dotenv
    
    env_file = get_project_root() / ".env"
    if env_file.exists():
        load_dotenv(env_file)
    else:
        print("⚠️ .env file not found. Using defaults.")


def format_feedback(analysis_dict: Dict) -> str:
    """Format analysis dictionary into readable feedback"""
    if not analysis_dict:
        return "No analysis available."
    
    formatted = ""
    for key, value in analysis_dict.items():
        formatted += f"\n### {key.replace('_', ' ').title()}\n"
        formatted += f"{value}\n"
    
    return formatted
