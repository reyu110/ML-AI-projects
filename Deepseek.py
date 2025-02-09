import ollama
import pandas as pd
import torch
import os

all_deepseek_responses = []  # Store response

# Free GPU memory before running Ollama
torch.cuda.empty_cache()

# Store all responses in a single list
data = []
desiredModel = 'deepseek-r1:1.5b'
questions = [
  f'Can you explain string theory?'
        ]

for question in questions:
    try:
      response = ollama.chat(model=desiredModel, messages=[{'role': 'user', 'content': question}])
      ollama_response = response.get('message', {}).get('content', 'No response')
      data.append({'Question': question, 'Response': ollama_response})
    except Exception as e:
      print(f"Error querying Deepseek AI: {e}")

all_deepseek_responses.extend(data)  # Append to global list

# Save DeepSeek responses for all tickers
deep_df = pd.DataFrame(all_deepseek_responses)
deep_output_file = "deepseek_responses.csv"
deep_df.to_csv(os.path.join(deep_output_file), index=False)
print("DeepSeek results saved for all tickers")
