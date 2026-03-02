# LocalRAG


### Table of Contents
----
1. [Project Overview](#projectoverview)
2. [What is RAG](#rag)
3. [Getting Started](#gettingstarted)
	- [Prerequisites](#prerequisites)
	- [Installation](#installation)
	- [Using your documents](#documents)
	- [Running the AI](#running)
4. [Contact](#contact)

### <a name="projectoverview"></a>Project Overview
----
A private AI assistant powered by your own documents. Ask questions and get fast, context-aware answers directly from your knowledge base

*Note: Currently the models only answer in Spanish for convenience, but it can be easily changed*

*Work in Progress!: Currently working on making Ollama start/stop automatically when running the main script*


### <a name="rag"></a>What is RAG
---
**Retrieval-Augmented Generation (RAG)** is a hybrid AI approach that combines **document retrieval** with **language generation** to produce accurate, context-aware responses. The workflow typically involves three main stages:

1. **Document Processing:**  
    The documents are first preprocessed and converted into a structured format. Each document is split into chunks, and an **embedding** (a numerical representation capturing semantic meaning) is generated for each chunk. These embeddings are stored in a **vector database** to allow fast similarity searches.
    
2. **Retrieval:**  
    When a user asks a question, the system converts the query into an embedding and searches the vector database for the most relevant document chunks. This ensures that the AI only has access to **contextually relevant information** when generating an answer.
    
3. **Generation:**  
    The retrieved chunks are passed to a **language model**, which synthesizes the information and produces a coherent, natural-language response. The model is guided to use **only the retrieved context**, making its answers grounded in the source documents rather than relying purely on memorized knowledge.
    

By combining retrieval and generation, RAG enables **AI systems to handle large knowledge bases efficiently**, provide **accurate answers**, and remain **up-to-date with private or specialized data** without needing to fine-tune the model.


### <a name="gettingstarted"></a>Getting Started
---

#### <a name="prerequisites"></a>Prerequisites

To be able to run the project, make sure to have the following tools installed:  

- **Ollama**:  
	Go to https://ollama.com/download and select your platform
	
- **AI model of preference**:  
	Run `` ollama pull gemma3:1b `` and `` ollama pull gemma3:4b `` on the terminal, to be able to run the tool on both modes.
	
	*Note: If your PC has low resources, download only gemma3:1b. You won’t be able to perform deeper searches, but it will still work.*


#### <a name="installation"></a>Installation

1.  Clone the repository:  
	```
	git clone https://github.com/Terzer-bit/LocalRAG.git
	```  
2. Change directory to the project folder:  
	```
	cd LocalRAG
	```
3. Install the requirements: 

	If you’re only testing this project or don’t plan to keep it installed, it is recommended to use a Python virtual environment. Run the following commands before installing the requirements:
	
	`` python -m venv myenv `` To create the virtual environment
	`` ./myenv/Scripts/activate ``  To activate the environment on Windows
	`` source myenv/bin/activate `` To activate the environment on Linux/MacOS

	```
	pip install -r requirements.txt 
	```  


#### <a name="documents"></a>Using your documents

1. Move all the desired documents to the folder ``documents`` inside this repository

	*Note: This project supports the following formats:* ``.txt``, ``.pdf``, ``.doc`` *and* ``.docx`` 

2. Run the ingestion script to create the vector database:
```
python ingest.py
```

Please note that any time a change is made inside the `documents` folder after the first ingestion, the files won’t be usable unless the ingestion script is run again.


#### <a name="running"></a>Running the AI

Once the documents are properly set up, you can run the RAG with a single command:

```
chainlit run app.py
```

### <a name="contact"></a>Contact
---
For any details contact the owner of the project on:
- Email: garciavinapablo@gmail.com
- LinkedIn: [pablo-garcía-viña](https://www.linkedin.com/in/pablo-garc%C3%ADa-vi%C3%B1a/)
