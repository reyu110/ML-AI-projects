# DeepSeek AI Chat with Ollama

Note: Deepseek_clean.py removes the reasoning text when saving.

This project queries the **DeepSeek AI** model using **Ollama**, processes the responses by cleaning unwanted text, and saves the results in a CSV file.

## Features
- Uses **Ollama** to interact with DeepSeek AI.
- Cleans AI responses by removing unnecessary text.
- Saves the responses to a CSV file for further analysis.
- Handles GPU memory management for better performance.

## Prerequisites
Before running the script, ensure you have the following installed:

- Python 3.8+
- `ollama` package (for AI queries)
- `pandas` (for data processing)
- `torch` (for GPU memory management)

### Install Dependencies
Run the following command to install required libraries:
```bash
pip install pandas torch
```
Additionally, install **Ollama** by following the instructions from the [Ollama website](https://ollama.com).

## Usage

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/deepseek-ollama.git
cd deepseek-ollama
```

### 2. Check Model Compatibility
Before pulling the DeepSeek model, ensure that your hardware can support it. DeepSeek AI models come in different sizes, and you should choose the one that fits your system's GPU/CPU capabilities.

#### Available Model Sizes & Pull Commands:
- **DeepSeek 1.5B** (for standard GPUs):
  ```bash
  ollama pull deepseek-r1:1.5b
  ```
- **DeepSeek 7B** (for higher-end GPUs with more VRAM):
  ```bash
  ollama pull deepseek-r1:7b
  ```
- **DeepSeek 8B** (for mid-range GPUs):
  ```bash
  ollama pull deepseek-r1:8b
  ```
- **DeepSeek 14B** (for high-performance GPUs):
  ```bash
  ollama pull deepseek-r1:14b
  ```
- **DeepSeek 32B** (for advanced AI workstations):
  ```bash
  ollama pull deepseek-r1:32b
  ```
- **DeepSeek 70B** (for powerful AI servers):
  ```bash
  ollama pull deepseek-r1:70b
  ```

Check your GPU VRAM and choose accordingly. Running a model that exceeds your hardware capacity may cause performance issues or failures.

### 3. Pull the DeepSeek Model
Once you've determined the appropriate model size, pull it using Ollama:
```bash
ollama pull deepseek-r1:1.5b  # Replace with the model size you need
```

### 4. Run the Script
```bash
python deepseek_chat.py
```

### 5. Output
- The script will send a predefined list of questions to the DeepSeek AI model.
- Responses will be cleaned and saved to `deepseek_responses.csv` in the project directory.

## Code Breakdown
1. **Frees GPU memory** using `torch.cuda.empty_cache()`.
2. **Queries DeepSeek AI** using the `ollama.chat()` function.
3. **Cleans responses** by removing text between `<think>` tags.
4. **Saves results to CSV** using Pandas.
5. **Handles errors** to prevent script failure.

## Example Output
The CSV file will look like this:
```csv
Question,Response
"Can you explain string theory?","String theory is a theoretical framework ..."
```

## Future Improvements
- Implement a CLI for dynamic question input.
- Integrate logging for better error tracking.
