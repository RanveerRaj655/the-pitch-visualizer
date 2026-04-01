import os
from huggingface_hub import InferenceClient

def refine_prompt(scene_text: str, style: str) -> str:
    """
    Given a scene description and a style, uses the Mistral LLM to generate 
    a highly detailed image generation prompt.
    """
    token = os.environ.get("HF_TOKEN")
    fallback_prompt = f"{scene_text}, {style}, cinematic lighting, highly detailed, 4K"
    
    if not token or token == "your_huggingface_token_here":
        return fallback_prompt
        
    client = InferenceClient(model="mistralai/Mistral-7B-Instruct-v0.3", token=token)
    
    system_instruction = "You are a visual prompt engineer. Given a scene description, return ONLY a single, highly detailed, visually rich image generation prompt. Include: lighting conditions, color palette, perspective/camera angle, artistic style, mood, and specific visual elements. Do not include any explanation or preamble. Output only the prompt itself."
    user_message = f"Scene: {scene_text}\nStyle: {style}\nReturn only the image prompt:"
    
    try:
        response = client.chat_completion(
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": user_message}
            ],
            max_tokens=200,
            temperature=0.7
        )
        prompt = response.choices[0].message.content.strip()
        if not prompt:
            raise ValueError("Empty response received from LLM")
        return prompt
    except Exception as e:
        print(f"Error generating prompt: {e}")
        return fallback_prompt
