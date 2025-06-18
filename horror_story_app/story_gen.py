import google.generativeai as genai

# ✅ Configure with your API key
genai.configure(api_key="AIzaSyBRFsYQpM5EKCjYIKCoHiBE7-fiBDMdWsk")

# ✅ Use the most powerful recent model for text generation
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_story(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating story: {e}"
