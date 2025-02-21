# ML-AI-projects
# DeepSeek AI Chat with Ollama

Note: Deepseek_clean.py has automated removal of reasoning text. If Reasoning text is required please use Deepseek.py

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

### 2. Run the Script

```bash
python deepseek_chat.py
```

### 3. Output

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

- Add support for multiple AI models.
- Implement a CLI for dynamic question input.
- Integrate logging for better error tracking.

## License

This project is licensed under the MIT License. Feel free to contribute and improve it!

---

For any questions or improvements, feel free to open an issue or submit a pull request!

