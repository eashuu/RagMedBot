<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
        <li>Python 3.12</li>
        <li>langchain</li>
        <li>PyPDF</li>
        <li>CTransformers and sentence-transformers</li>
        <li>Chainlit</li>
        <li>faiss_cpu</li>
        <li>Other dependencies as specified in <code>requirements.txt</code></li>
    </ul>
    
  <h2>Installation</h2>
    <ol>
        <li>Clone the repository:</li>
        <pre><code>git clone https://github.com/your-username/medical-chatbot.git</code></pre>
        <li>Install dependencies:</li>
        <pre><code>pip install -r requirements.txt</code></pre>
        <li>Install the quantized llama2 model from HuggingFace:
        <pre><a href="https://huggingface.co/TheBloke/Llama-2-7B-GGML/blob/main/llama-2-7b.ggmlv3.q8_0.bin">https://huggingface.co/TheBloke/Llama-2-7B-GGML/blob/main/llama-2-7b.ggmlv3.q8_0.bin</a></pre></li>
    </ol>

  <h2>Usage</h2>
    <ol>
        <li>Run the ingest.py file to create vectorstores:</li>
        <pre><code>python ingest.py</code></pre>
        <li>Now run the chatbot model:.</li>
        <pre><code>chainlit run model.py</code></pre>
        <li>Input your medical queries and receive accurate responses.<br>
        Note:This model has been built solely for the purpose of clinical question and answering thus it cannot answer questions irrelevant to medical queries</li>
    </ol>

  <h2>File Structure</h2>
    <ul>
        <li><code>model.py</code>: Main script to run the chatbot.</li>
        <li><code>ingest.py</code>: Script for ingesting data into vectorstores.</li>
        <li><code>vectorstores/</code>: Directory containing vector stores for efficient storage and retrieval of embeddings.</li>
        <li><code>data/</code>: Directory containing the medical PDF dataset.</li>
        <li><code>requirements.txt</code>: List of Python dependencies.</li>
    </ul>

   <h2>Acknowledgements</h2>
    <ul>
        <li><a href="https://huggingface.co/TheBloke/Llama-2-7B-GGML/blob/main/llama-2-7b.ggmlv3.q8_0.bin">Llama2-7b Model by TheBloke</a></li>
        <li><a href="https://github.com/chainlit/chainlit">Chainlit Library</a></li>
    </ul>

  <h2>Contributing</h2>
    <p>Contributions are welcome! Please feel free to submit pull requests.</p>

  
</div>

</body>
</html>
