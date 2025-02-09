import ollama
import pandas as pd
import torch
import os
import re  # Import regex module

# Free GPU memory before running Ollama
torch.cuda.empty_cache()

# Store responses
all_deepseek_responses = []

# Select the desired model
desiredModel = 'deepseek-r1:1.5b'
questions = [
    "Can you write me an article blog that is over 1,500 words long on the latest news in tech? Make sure to add some personality and character into it and discuss opinions in the blog. Make sure the blog is more than 1,500 words long. Make sure to not include mention anything about the age, gender or personal information about the author."
]

# Function to clean response text
def clean_response(text):
    """Removes all text between </think> tags using regex."""
    return re.sub(r"</think>.*?</think>", "", text, flags=re.DOTALL).strip()

# Query DeepSeek AI
for question in questions:
    try:
        response = ollama.chat(model=desiredModel, messages=[{'role': 'user', 'content': question}])
        ollama_response = response.get('message', {}).get('content', 'No response')
        
        # Clean response
        cleaned_response = clean_response(ollama_response)
        
        all_deepseek_responses.append({'Question': question, 'Response': cleaned_response})
    except Exception as e:
        print(f"Error querying Deepseek AI: {e}")

# Save responses to CSV
deep_df = pd.DataFrame(all_deepseek_responses)
deep_output_file = "Skimpy_blog_cleaned.csv"
deep_df.to_csv(deep_output_file, index=False)
print("DeepSeek results saved with cleaned responses")
