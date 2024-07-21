# Jessup Cellars Chatbot

This repository contains the code for the Jessup Cellars Chatbot, a sophisticated conversational agent designed for a wine business. The chatbot leverages advanced Natural Language Processing (NLP) and Deep Learning techniques to provide users with information about wines, visiting hours, events, and more.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Skills Utilized](#skills-utilized)
- [License](#license)

## Overview

The Jessup Cellars Chatbot is built using Flask for the backend, SocketIO for real-time communication, and a fine-tuned GPT-2 model for generating responses. It also uses Spacy for NLP tasks and integrates TF-IDF vectorization and cosine similarity for handling user queries effectively.

## Features

- **Real-time Chat Interface**: Users can interact with the chatbot through a web-based interface.
- **Wine Information**: Provides detailed information about different wines.
- **Visiting Hours**: Answers queries regarding the business's visiting hours and location.
- **Events and Experiences**: Information about events and experiences offered by the business.
- **Membership Details**: Details about the wine club membership.


## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/jessup-cellars-chatbot.git
    cd jessup-cellars-chatbot
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Download the fine-tuned GPT-2 model**:
    ```bash
    python load_model_test.py
    ```

5. **Run the application**:
    ```bash
    python app.py
    ```

6. **Open your browser** and navigate to `http://127.0.0.1:5000`.

## Usage

- **Interact with the chatbot**: Type your queries into the chat interface and receive instant responses.
- **Intents**: Use predefined buttons to ask about wine information, visiting hours, events, and more.

## Project Structure

```
jessup-cellars-chatbot/
│
├── models/
│   └── fine_tuned_gpt/
│       └── checkpoint-15/
│           ├── config.json
│           ├── pytorch_model.bin
│           └── tokenizer_config.json
│
├── data/
│   └── corpus.json
│
├── templates/
│   └── index.html
│
├── static/
│   ├── styles.css
│   └── script.js
│
├── app.py
├── load_model_test.py
├── requirements.txt
└── README.md
```

## Skills Utilized

- **Natural Language Processing (NLP)**: Using Spacy for text preprocessing and understanding.
- **Deep Learning**: Fine-tuned GPT-2 model for generating responses.
- **Web Development**: Flask and SocketIO for building the web-based chat interface.
- **Machine Learning**: TF-IDF vectorization and cosine similarity for query matching.
- **Python Programming**: Integrating various libraries and frameworks to create a seamless chatbot experience.



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


