import ollama
import pandas as pd
import torch
import os
import re

all_deepseek_responses = []  # Store response

# Free GPU memory before running Ollama
torch.cuda.empty_cache()

# Store all responses in a single list
data = []
desiredModel = 'deepseek-r1:1.5b'
questions = [
  f'Can you explain string theory?'
        ]

# Function to clean response text
def clean_response(text):
    """Removes all text between </think> tags using regex."""
    return re.sub(r"</think>.*?</think>", "", text, flags=re.DOTALL).strip()

for question in questions:
    try:
      response = ollama.chat(model=desiredModel, messages=[{'role': 'user', 'content': question}])
      ollama_response = response.get('message', {}).get('content', 'No response')
      # Clean response
      cleaned_response = clean_response(ollama_response)

      all_deepseek_responses.append({'Question': question, 'Response': cleaned_response})
    except Exception as e:
        print(f"Error querying Deepseek AI: {e}")


all_deepseek_responses.extend(data)  # Append to global list

# Save DeepSeek responses for all tickers
deep_df = pd.DataFrame(all_deepseek_responses)
deep_output_file = "deepseek_responses.csv"
deep_df.to_csv(os.path.join(deep_output_file), index=False)
print("DeepSeek results saved for all tickers")
