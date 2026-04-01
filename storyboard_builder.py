from pathlib import Path
from segmenter import segment_text
from prompt_engineer import refine_prompt
from image_generator import generate_image

def build_storyboard(text: str, style: str) -> list[dict]:
    """
    Orchestrates the storyboard generation process:
    1. Segments text
    2. Refines prompts sequentially
    3. Generates images sequentially
    Returns a list of panel dictionaries.
    """
    sentences = segment_text(text)
    panels = []
    
    # Ensure static/panels directory exists before saving generated images
    output_dir = Path("static") / "panels"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for i, scene_text in enumerate(sentences):
        panel_index = i + 1
        refined_prompt = refine_prompt(scene_text, style)
        image_url = generate_image(refined_prompt, panel_index, output_dir)
        
        panels.append({
            "index": panel_index,
            "scene_text": scene_text,
            "refined_prompt": refined_prompt,
            "image_url": image_url
        })
        
    return panels
