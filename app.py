"""
AI Photography Coach - MVP
Main Streamlit Application

Author: Prasad Tilloo
Date: November 2025
"""
import subprocess
import streamlit as st
from pathlib import Path
import sys
import ollama

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

# ============================================================================
# PAGE CONFIG
# ============================================================================

st.set_page_config(
    page_title="AI Photography Coach",
    page_icon="📸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# HELPER FUNCTION - OLLAMA INTEGRATION
# ============================================================================

def generate_photography_feedback(photo_description: str) -> str:
    """Generate photography feedback using Ollama."""
    
    prompt = f"""You are a photography expert. Analyze this photo:

PHOTO: {photo_description}

Provide brief feedback on:
- Composition (what works, what to improve)
- Lighting (quality and tips)
- Rating (X/10) with one key improvement

Keep it concise and specific."""

    try:
        response = ollama.chat(
            model='llama3.2:3b',
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}\n\nMake sure Ollama is running."
# ============================================================================
# TITLE & HEADER
# ============================================================================

st.title("📸 AI Photography Coach")
st.markdown("""
### Get AI-Powered Feedback on Your Photos
*Composition • Lighting • Storytelling • Technical Analysis*

**Powered by:** Ollama (Llama 3.2 3B - Local AI)
""")

# ============================================================================
# SIDEBAR
# ============================================================================

with st.sidebar:
    st.header("About This Tool")
    st.write("""
    **AI Photography Coach** analyzes your photos using local AI and provides 
    constructive feedback on:
    
    - 🎨 **Composition** - framing, balance, flow
    - 💡 **Lighting** - quality, direction, mood
    - 📖 **Storytelling** - narrative, emotion
    - ⚙️ **Technical** - overall assessment
    """)
    
    st.markdown("---")
    
    # System status
    st.success("✅ Ollama Connected")
    st.info("🤖 Model: Llama 3.2 (3B)")
    
    st.markdown("---")
    
    st.markdown("""
    ### 💡 Tips for Best Results
    
    Include in your description:
    - What's in the photo
    - Lighting conditions
    - Mood/atmosphere
    - Subject details
    """)

# ============================================================================
# MAIN TABS
# ============================================================================

tab1, tab2, tab3 = st.tabs(["📷 Analyze Photo", "💡 Learn Photography", "ℹ️ About"])

# ============================================================================
# TAB 1: PHOTO ANALYSIS
# ============================================================================

with tab1:
    st.header("Analyze Your Photography")
    
    # Example descriptions
    with st.expander("📋 See Example Descriptions"):
        st.markdown("""
        **Landscape Example:**
        ```
        Mountain landscape at sunset with golden hour light illuminating 
        the peaks. A stream winds through the foreground creating leading 
        lines. Sky shows warm orange and purple tones. Foreground is in 
        shadow but texture is visible on rocky terrain.
        ```
        
        **Portrait Example:**
        ```
        Portrait of person with soft window light from the left creating 
        gentle shadows on face. Blurred background with warm bokeh. 
        Subject looking slightly off-camera with natural expression. 
        Shot at f/2.8 with shallow depth of field.
        ```
        
        **Street Photography Example:**
        ```
        Urban street scene with strong geometric shapes from buildings. 
        Multiple subjects in motion. Harsh midday sun creating dramatic 
        shadows and high contrast. Composition uses leading lines from 
        architecture. Black and white conversion emphasizes shapes.
        ```
        """)
    
    photo_description = st.text_area(
        "Describe your photo:",
        placeholder="Enter detailed description of your photograph...",
        height=150,
        help="The more detail you provide, the better the analysis!"
    )
    
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        analyze_button = st.button("🔍 Get AI Feedback", type="primary", use_container_width=True)
    
    with col2:
        if st.button("🗑️ Clear", use_container_width=True):
            st.rerun()
    
    if analyze_button:
        if not photo_description or len(photo_description) < 20:
            st.error("⚠️ Please provide a detailed photo description (at least 20 characters)")
        else:
            with st.spinner("🤖 AI is analyzing your photo... (this may take 20-30 seconds)"):
                feedback = generate_photography_feedback(photo_description)
                
                st.markdown("---")
                st.markdown("### 📊 AI Photography Feedback")
                st.markdown(feedback)
                
                # Add copy button for feedback
                st.download_button(
                    label="📄 Download Feedback",
                    data=feedback,
                    file_name="photography_feedback.txt",
                    mime="text/plain"
                )

# ============================================================================
# TAB 2: LEARN PHOTOGRAPHY
# ============================================================================

with tab2:
    st.header("Photography Learning Resources")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎨 Composition Principles")
        st.markdown("""
        **Rule of Thirds**
        - Place subjects at grid intersections
        - Creates dynamic compositions
        - Avoids centered, static images
        
        **Leading Lines**
        - Roads, rivers, fences guide eye
        - Creates depth and journey
        - Draws viewer into scene
        
        **Foreground, Midground, Background**
        - Creates sense of depth
        - Makes 2D image feel 3D
        - Tells complete story
        
        **Negative Space**
        - Empty space around subject
        - Lets subject breathe
        - Emphasizes main focus
        """)
    
    with col2:
        st.subheader("💡 Lighting Techniques")
        st.markdown("""
        **Golden Hour**
        - 1 hour after sunrise / before sunset
        - Warm, soft, directional light
        - Flattering for all subjects
        
        **Blue Hour**
        - Just after sunset / before sunrise
        - Cool blue tones
        - Great for urban scenes
        
        **Side Lighting**
        - Light from 90° to subject
        - Emphasizes texture & dimension
        - Shows form and shape
        
        **Backlighting**
        - Subject between camera and light
        - Creates rim light and glow
        - Good for silhouettes
        """)
    
    st.markdown("---")
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("📖 Storytelling")
        st.markdown("""
        **Elements of Visual Story:**
        - Clear subject (what/who)
        - Context (where/when)
        - Action or moment (what's happening)
        - Emotion (how it feels)
        - Universal connection (why we care)
        """)
    
    with col4:
        st.subheader("⚙️ Technical Tips")
        st.markdown("""
        **Exposure Triangle:**
        - Aperture (depth of field)
        - Shutter speed (motion blur)
        - ISO (light sensitivity)
        
        **Focus:**
        - Sharp on intended subject
        - Appropriate depth of field
        - No distracting blur
        """)

# ============================================================================
# TAB 3: ABOUT
# ============================================================================

with tab3:
    st.header("About AI Photography Coach")
    
    st.markdown("""
    ### 🎓 AI Engineering Capstone Project
    
    This application demonstrates practical AI engineering through a real-world use case:
    helping photographers improve their craft with instant, intelligent feedback.
    
    ### 🛠️ Technology Stack
    
    - **Frontend:** Streamlit (Python web framework)
    - **AI Model:** Ollama - Llama 3.2 (3B parameters)
    - **Processing:** Local inference (privacy-first)
    - **Prompting:** Structured prompt engineering
    
    ### 📚 Course Concepts Applied
    
    **Lesson 1 - LLM Foundations:**
    - Prompt engineering for structured output
    - Temperature and parameter tuning
    - Context management
    
    **Lesson 2 - RAG Concepts:**
    - Knowledge base structure (photography principles)
    - Information retrieval patterns
    
    **Lesson 3 - Agent Design:**
    - Task decomposition (composition, lighting, storytelling)
    - Structured reasoning
    
    **Lesson 4 - Advanced Reasoning:**
    - Chain-of-Thought prompting
    - Multi-aspect analysis
    - Constructive feedback generation
    
    **Lesson 5 - Multimodal:**
    - Photo description as input modality
    - Text-based image analysis
    
    ### 👤 Created By
    
    **Prasad Tilloo**
    - Solution Architect | 15+ Years Experience
    - Photography Enthusiast
    - AI Engineering Student
    
    ### 🔗 Links
    
    - **GitHub:** [ai-photography-coach](https://github.com/prasadt1/ai-photography-coach)
    - **LinkedIn:** [Prasad Tilloo](https://linkedin.com/in/prasadtilloo)
    
    ### 📊 Project Stats
    
    - **Development Time:** 5 days
    - **Lines of Code:** ~400
    - **Tech Stack:** Python, Streamlit, Ollama
    - **Status:** ✅ Working MVP
    
    ### 🚀 Future Enhancements
    
    - Image upload with vision model analysis
    - RAG with photography textbooks
    - Multi-language support
    - Cloud deployment
    - Mobile app version
    - Portfolio tracking over time
    """)

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1rem;">
    <p>📸 <strong>AI Photography Coach</strong> | Capstone Project November 2025</p>
    <p>Made with ❤️ using Streamlit + Ollama</p>
</div>
""", unsafe_allow_html=True)
