<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Medical Chatbot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 800px;
            margin: 20px auto;
            padding: 0 20px;
        }
        h1, h2, h3 {
            color: #333;
        }
        h2 {
            border-bottom: 1px solid #ccc;
            padding-bottom: 5px;
        }
        ul {
            padding-left: 20px;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 5px;
            border-radius: 3px;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Medical Chatbot</h1>
    
  <h2>Overview</h2>
    <p>This repository contains the code for a medical chatbot that utilizes retrieval-augmented generation techniques. The chatbot is designed to provide medical information based on a given input query. It is built using a pre-trained quantized Llama2 model and runs efficiently on CPU.</p>
    
  <h2>Features</h2>
    <ul>
        <li><strong>Retrieval-Augmented Generation</strong>: The chatbot employs retrieval-augmented generation techniques to provide accurate responses to user queries.</li>
        <li><strong>Medical PDF Integration</strong>: It is trained using a dataset derived from medical PDF documents, ensuring the accuracy and relevance of responses to medical queries.</li>
        <li><strong>Efficient CPU Execution</strong>: The model is quantized to run efficiently on CPU, making it accessible for deployment on a wide range of platforms.</li>
        <li><strong>Chainlit Integration</strong>: Chainlit library is used for seamless integration of retrieval and generation components, enhancing the performance and reliability of the chatbot.</li>
    </ul>
    
  <h2>Requirements</h2>
    <p>To run this project, you need:</p>
    <ul>
        <li>Python 3.x</li>
        <li>PyTorch</li>
        <li>Chainlit</li>
        <li>Other dependencies as specified in <code>requirements.txt</code></li>
    </ul>
    
  <h2>Installation</h2>
    <ol>
        <li>Clone the repository:</li>
        <pre><code>git clone https://github.com/your-username/medical-chatbot.git</code></pre>
        <li>Install dependencies:</li>
        <pre><code>pip install -r requirements.txt</code></pre>
    </ol>

  <h2>Usage</h2>
    <ol>
        <li>Run the chatbot:</li>
        <pre><code>python chatbot.py</code></pre>
        <li>Follow the instructions to interact with the chatbot.</li>
        <li>Input your medical queries and receive accurate responses.</li>
    </ol>

  <h2>File Structure</h2>
    <ul>
        <li><code>chatbot.py</code>: Main script to run the chatbot.</li>
        <li><code>model.py</code>: Contains the definition of the quantized Llama2 model.</li>
        <li><code>utils.py</code>: Utility functions for data preprocessing and inference.</li>
        <li><code>data/</code>: Directory containing the medical PDF dataset.</li>
        <li><code>requirements.txt</code>: List of Python dependencies.</li>
    </ul>

   <h2>Acknowledgements</h2>
    <ul>
        <li><a href="https://github.com/llamalu/llama2">Llama2 Model</a></li>
        <li><a href="https://github.com/chainlit/chainlit">Chainlit Library</a></li>
    </ul>

   <h2>License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

  <h2>Contributing</h2>
    <p>Contributions are welcome! Please feel free to submit pull requests.</p>

  <h2>Authors</h2>
    <ul>
        <li><a href="https://github.com/your-username">Your Name</a></li>
    </ul>
</div>

</body>
</html>
