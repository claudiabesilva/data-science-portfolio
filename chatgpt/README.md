# ChatGPT Data Analysis

Exploratory data analysis of a ChatGPT-style instruction dataset (`vicgalle/alpaca-gpt4`) using Python and Jupyter.

## What this project covers

- Most frequent user prompt themes
- Prompt type categorization
- Response readability (Flesch Reading Ease)
- Relationship between prompt length and response length/complexity
- Verbosity analysis (words per sentence)
- Impact of extra context (`input`) on responses

## Dataset

- Source: [Hugging Face - `vicgalle/alpaca-gpt4`](https://huggingface.co/datasets/vicgalle/alpaca-gpt4)
- Approx. size: 52k rows
- Main fields: `instruction`, `input`, `output`, `text`

## Tools & Libraries

- Python, Jupyter Notebook
- pandas
- matplotlib / seaborn / plotly
- nltk
- wordcloud
- textstat

## Files

- `ChatGPT_DataAnalysis..ipynb` — full analysis notebook
- `README.md` — project documentation

## Run locally

```bash
pip install pandas matplotlib seaborn plotly nltk wordcloud textstat huggingface_hub pyarrow
