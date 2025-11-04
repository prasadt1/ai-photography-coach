"""
RAG Pipeline for Photography Knowledge Base
Day 1: Foundation & Structure
"""

from typing import List, Dict
from pathlib import Path


class PhotographyKnowledgeBase:
    """Photography knowledge base for RAG system"""
    
    COMPOSITION_KNOWLEDGE = """
    COMPOSITION PRINCIPLES:
    
    Rule of Thirds:
    - Divide frame into 3x3 grid
    - Place subjects at intersection points (1/3 or 2/3 of frame)
    - Creates more dynamic, engaging compositions
    - Moves subjects away from center, creating visual interest
    
    Leading Lines:
    - Roads, rivers, railroads, fences guide viewer's eye
    - Creates sense of depth and journey
    - Draws attention toward subject
    - Can be straight, curved, diagonal
    
    Foreground, Midground, Background:
    - Create depth by including all three layers
    - Foreground: immediate area near camera
    - Midground: subject and main focus area
    - Background: contextual elements
    - Creates three-dimensional feel on 2D image
    
    Framing:
    - Use natural elements to frame subject (trees, windows, arches)
    - Focuses viewer attention
    - Adds depth and context
    - Creates frame within the frame
    
    Symmetry vs Asymmetry:
    - Symmetry: calming, formal, peaceful
    - Asymmetry: dynamic, engaging, energetic
    - Choose based on intended emotion
    
    Negative Space:
    - Empty space around subject
    - Lets subject breathe
    - Can be as important as subject itself
    - Emphasizes subject through absence
    """
    
    LIGHTING_KNOWLEDGE = """
    LIGHTING TECHNIQUES:
    
    Golden Hour (Best Light):
    - 1 hour after sunrise OR 1 hour before sunset
    - Warm, soft, directional light
    - Creates beautiful color palette (warm oranges/golds)
    - Minimal shadows, flattering for portraits
    - Magical, romantic atmosphere
    
    Blue Hour:
    - Just after sunset OR just before sunrise
    - Cool blue tones
    - Balanced between sky and artificial lights
    - Moody, contemplative mood
    - Great for architecture, urban photography
    
    Side Lighting:
    - Light coming from side of subject (90° to camera)
    - Emphasizes texture and dimension
    - Creates modeling (3D appearance)
    - Good for portraits to show features
    - Defines shape and form
    
    Backlighting:
    - Subject between light source and camera
    - Creates rim light (glowing edge around subject)
    - Separates subject from background
    - Creates halo effect
    - Use for silhouettes at sunset
    
    Front Lighting:
    - Light directly behind camera toward subject
    - Even, flat illumination
    - Minimizes texture and dimension
    - Can be boring if not used creatively
    - Good for basic documentation
    
    Fill Light:
    - Secondary light to reduce shadow contrast
    - Brightens shadowed areas
    - Creates more flattering light
    - Can be reflector or secondary light source
    
    Harsh vs Soft Light:
    - Harsh: Direct sun, creates strong shadows (dramatic)
    - Soft: Overcast, shade, creates subtle shadows (flattering)
    - Time of day affects harshness
    - Modifiers (reflectors, diffusers) soften light
    """
    
    STORYTELLING_KNOWLEDGE = """
    STORYTELLING ELEMENTS:
    
    Subject & Context:
    - What is the main subject? (person, place, object)
    - What context surrounds it?
    - Does context enhance or distract?
    - Subject should be clear and intentional
    
    Emotional Impact:
    - What feeling does the image evoke?
    - Color affects emotion (warm=happy, cool=sad)
    - Composition affects emotion (tilted=tension, balanced=calm)
    - Lighting affects emotion (golden=peaceful, harsh=dramatic)
    
    Hierarchy:
    - What does viewer see first? (main subject)
    - What next? (secondary elements)
    - What last? (background/context)
    - Use contrast, color, sharpness to guide attention
    
    Narrative:
    - What's happening in the image?
    - Before this moment? After?
    - What story does viewer construct?
    - Is story clear or ambiguous?
    
    Human Connection:
    - Can viewer relate to image?
    - Does it evoke personal memories?
    - Is there universal element?
    - Why should viewer care?
    
    Authenticity:
    - Does image feel genuine?
    - Or posed/artificial?
    - Authentic moments are compelling
    - Directness communicates clearly
    """
    
    TECHNICAL_KNOWLEDGE = """
    TECHNICAL ASPECTS:
    
    Exposure:
    - Brightness of image (not too dark/bright)
    - Highlights not blown out (lost detail)
    - Shadows not crushed (lost detail)
    - Histogram shows distribution
    
    Focus & Sharpness:
    - Is main subject in sharp focus?
    - Is focus where you intended?
    - Depth of field appropriate?
    - Distracting blur elsewhere?
    
    Color Balance:
    - White balance corrects color temperature
    - Daylight vs tungsten affects color tone
    - Can be creative (intentional color cast)
    - Should feel natural unless artistic choice
    
    Composition & Framing:
    - No distracting elements in corners
    - Horizon level (unless intentional tilt)
    - Headroom appropriate in portraits
    - Cropping effective
    
    Noise & Grain:
    - Some noise acceptable with high ISO
    - Grain can be artistic at low ISO
    - Should not distract from subject
    - Can be creative element
    
    Color & Saturation:
    - Colors vivid without being oversaturated
    - Color palette cohesive
    - Contrast between colors effective
    - No color fringing or aberration
    """
    
    @classmethod
    def get_all_knowledge(cls) -> str:
        """Return all knowledge base"""
        return "\n\n".join([
            cls.COMPOSITION_KNOWLEDGE,
            cls.LIGHTING_KNOWLEDGE,
            cls.STORYTELLING_KNOWLEDGE,
            cls.TECHNICAL_KNOWLEDGE
        ])
    
    @classmethod
    def get_composition_knowledge(cls) -> str:
        """Return composition knowledge only"""
        return cls.COMPOSITION_KNOWLEDGE
    
    @classmethod
    def get_lighting_knowledge(cls) -> str:
        """Return lighting knowledge only"""
        return cls.LIGHTING_KNOWLEDGE
    
    @classmethod
    def get_storytelling_knowledge(cls) -> str:
        """Return storytelling knowledge only"""
        return cls.STORYTELLING_KNOWLEDGE
    
    @classmethod
    def get_technical_knowledge(cls) -> str:
        """Return technical knowledge only"""
        return cls.TECHNICAL_KNOWLEDGE


class PhotoAnalyzer:
    """Photo analysis using RAG"""
    
    def __init__(self):
        self.knowledge = PhotographyKnowledgeBase()
    
    def analyze_composition(self, photo_description: str) -> Dict:
        """Analyze photo composition"""
        # TODO: Implement RAG + LLM analysis (Day 2)
        return {"status": "coming_day_2"}
    
    def analyze_lighting(self, photo_description: str) -> Dict:
        """Analyze lighting"""
        # TODO: Implement RAG + LLM analysis (Day 2)
        return {"status": "coming_day_2"}
    
    def analyze_storytelling(self, photo_description: str) -> Dict:
        """Analyze storytelling"""
        # TODO: Implement RAG + LLM analysis (Day 2)
        return {"status": "coming_day_2"}
    
    def get_full_analysis(self, photo_description: str) -> Dict:
        """Get complete analysis"""
        # TODO: Implement full pipeline (Day 2)
        return {"status": "coming_day_2"}
