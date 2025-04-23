from final_code.config import llm

def review_content(input_text: str):
    prompt = f"Review the given content: {input_text}\nMake necessary corrections and rewrite in a positive tone."
    return llm.invoke(prompt)
