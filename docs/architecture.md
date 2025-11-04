# Technical Architecture - AI Photography Coach

## System Overview

The AI Photography Coach uses RAG (Retrieval-Augmented Generation) to provide 
intelligent feedback on photographic images.

## Components

### 1. User Interface (Streamlit)
- Photo upload
- Photo description input
- Analysis results display
- Learning resources

### 2. RAG Pipeline
- Photography knowledge base
- FAISS vector store
- Semantic search
- Context retrieval

### 3. LLM Analysis
- Ollama (Llama 3.2)
- Chain-of-Thought prompting
- Multi-aspect analysis

### 4. Output
- Structured feedback
- Example improvements
- Ratings


## Data Flow

[Photo Upload]
↓
[Photo Description Input]
↓
[RAG Retrieval - Get Photography Principles]
├─ Composition knowledge
├─ Lighting techniques
├─ Storytelling elements
└─ Technical aspects
↓
[LLM Analysis with CoT]
├─ "Let me think about the composition..."
├─ "Consider the lighting quality..."
├─ "The storytelling aspect..."
└─ "Technical assessment..."
↓
[Structure Output]
├─ Strengths (✅)
├─ Areas to improve (⚠️)
├─ Suggestions (💡)
└─ Rating (8/10)


## Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Frontend | Streamlit | Web UI |
| RAG | LangChain + FAISS | Knowledge retrieval |
| Embeddings | sentence-transformers | Semantic search |
| LLM | Ollama (Llama 3.2) | Analysis generation |
| Processing | PIL, OpenCV | Image handling |

## Key Features

1. **Multi-aspect Analysis**
   - Composition
   - Lighting
   - Storytelling
   - Technical

2. **Knowledge-Grounded**
   - All feedback based on photography principles
   - Specific examples from knowledge base
   - Educational and constructive

3. **Chain-of-Thought Reasoning**
   - Shows reasoning process
   - Explains why (not just what)
   - Transparent feedback

4. **Actionable Feedback**
   - Specific suggestions
   - Not generic platitudes
   - Helps photographers improve
