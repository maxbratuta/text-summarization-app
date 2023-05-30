# Text Summarization App

This project focuses on text summarization, which aims to generate concise and coherent summaries based on client text.

<img height="512" alt="image" src="https://github.com/maxbratuta/text-summarization-app/assets/45269875/35a11c3a-76fb-43c2-9aa2-a16c68900c5c">


<br />

## Technologies Used
* **Transformers Library**: The Transformers library, developed by [Hugging Face](https://huggingface.co/transformers/v4.10.1/task_summary.html#summarization), is utilized for its state-of-the-art pre-trained models for text generation and summarization.
* **Python**
* **Flask**
* **HTML / JS / CSS**

<br />

## Steps

**Step 1.** Clone this repository - https://github.com/maxbratuta/text-summarization-app.

**Step 2.** Create a new virtual environment.

```
# Default
python3 -m venv text-summarization

# Anaconda
conda create --name text-summarization -y
```

**Step 3.** Activate your virtual environment.

```
# Default
source text-summarization/bin/activate 

# Anaconda
conda activate text-summarization
```

**Step 4.** Install dependencies and add virtual environment to the Python Kernel.

```
# Default
python3 -m pip install --upgrade pip
pip install transformers flask

# Anaconda
conda install transformers flask -y
```

**Step 5.** Run Flask server.
```
python app.py
```

**Step 6.** Open your local site in a browser.
```
http://127.0.0.1:8000
```

**Step 7.** Make a text summarization.
- **Step 7.1.** Copy an example article below and paste into the text box or provide your own
    <br /><br />
    ****DISCLAIMER.*** This text was taken as a random example and does not have an advertising nature. Link to the author's article page in the text.*
    
    ```
    Analysis does not require critical tools and methods always.
    Link: https://medium.com/@keyurjoshi25/analysis-does-not-require-critical-tools-and-methods-always-624e7c30b482
    
    Hello there! 
    This is my very first post and what made me write this title is the essence of running in the race too fast without knowing the fundamentals or concepts. 
    Keep things simple and see the miracle.
    
    My name is Keyur Joshi, having keen interest in product and business analytics and enhancements. 
    There are plenty of incidents where I found people too much involved into critical thinking while doing the analysis using any of those trending tools. 
    And this brought me here to write up and keep things simple for those who are finding it difficult in analysis. 
    Especially, the new bees, freshers, entrants, enthusiasts or the ones who are having interest in “How to read and understand the data?” this could be a thoughtful post for easier productivity and standing out uncommon.
    ```

- **Step 7.2.** Click on the Summarize button and wait for some time.
- **Step 7.3.** As a result, you will see the generated summary text below.
