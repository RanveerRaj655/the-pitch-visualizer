# The Pitch Visualizer

The Pitch Visualizer is a production-ready web application that transforms narrative text into visually rich storyboards. It uses NLTK to segment the text into distinct scenes, `mistralai/Mistral-7B-Instruct-v0.3` to engineer highly detailed image prompts, and `black-forest-labs/FLUX.1-dev` to generate vivid panel images. The resulting scenes are beautifully rendered in a dynamic HTML interface, complete with print-to-PDF functionality.

## Architecture

Text → Segmenter → [Scene 1..N] → LLM Prompt Engineer → FLUX Image Generator → HTML Storyboard

## Setup Instructions

### 1. Get a HuggingFace Token
1. Go to [huggingface.co](https://huggingface.co) and sign in.
2. Navigate to **Settings** → **Access Tokens**.
3. Click **New token** and create one with the **Read** role.

### 2. Windows Installation
Open PowerShell or Command Prompt in the project folder and run the following commands:
```bat
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```
Edit `.env` and paste your HuggingFace token.

### 3. Run the App
```bat
uvicorn main:app --reload
```
Navigate to `http://localhost:8000` in your web browser.

## Style Modes

| Visual Style | Appended Keywords/Attributes | Ideal Use Case |
| ------------- | ------------- | ------------- |
| Cinematic Photorealistic | cinematic lighting, highly detailed, 4K | Dramatic sales pitches, high-end product stories |
| Digital Art Illustration | vibrant colors, stylized, creative | Concept art, imaginative storytelling |
| Watercolor Painting | soft edges, washed colors, artistic | Emotional narratives, soft branding |
| Noir Black and White | high contrast, moody shadow, monochrome | Mystery, suspense, dramatic testimonials |
| Corporate Flat Design | vector, clean lines, minimalist | B2B pitches, explainer videos, clean UI |

## Design Rationale
Using an LLM for prompt refinement ensures that simple sentence fragments are expanded into rich, descriptive image prompts. Raw narrative text often lacks the visual descriptors required for high-quality text-to-image synthesis. The LLM acts as an intermediate "director," explicitly defining lighting, mood, color palette, and framing, maximizing the generation capabilities of the FLUX.1 model.
