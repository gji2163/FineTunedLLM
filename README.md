# LibrarianAI

## Overview

This web application utilizes a Large Language Model (LLM) to generate text-based content. The model is trained on the content of the book '48 Laws of Power', which is available as a PDF [here](https://pgcag.files.wordpress.com/2010/01/48lawsofpower.pdf).

The primary functionality of the web app is to answer questions related to the content of the book using the trained language model.

## Features

- Text generation powered by OpenAI's GPT-4.
- Supports question answering based on the content of the book, '48 Laws of Power'.
- User-friendly web interface for inputting questions and receiving answers.
- Web Access
- Multiple Themes

## Getting Started

### Prerequisites

- Python 3.x
- OpenAI API key
- flask
- requests

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/gji2163/FineTunedLLM.git
    cd FineTunedLLM
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your OpenAI API key:

    ```bash
    export OPENAI_API_KEY="your-api-key"
    ```

### Usage

1. Run the web application:

    ```bash
    python app.py
    ```

2. Access the web app in your browser at `http://localhost:1338`.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please create an issue or submit a pull request.
