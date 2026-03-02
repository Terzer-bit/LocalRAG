import os
import shutil
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    Docx2txtLoader,
    UnstructuredWordDocumentLoader
)

# --- CONFIGURATION ---
DOCS_FOLDER = "./documents"
DB_PATH = "./chroma_db"

def load_documents():
    # 1. Initialize Embeddings
    print("Initializing embedding model...")
    embeddings = OllamaEmbeddings(model="nomic-embed-text:v1.5")

    # 2. Initialize Database
    # We use valid persistent directory to store data
    vectorstore = Chroma(
        collection_name="my_knowledge_base",
        embedding_function=embeddings,
        persist_directory=DB_PATH
    )

    # 3. Setup Splitter
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

    # 4. Check for documents folder
    if not os.path.exists(DOCS_FOLDER):
        os.makedirs(DOCS_FOLDER)
        print(f"Created folder '{DOCS_FOLDER}'. Please put your files inside and run again.")
        return

    # 5. Get list of files
    files = [f for f in os.listdir(DOCS_FOLDER) if os.path.isfile(os.path.join(DOCS_FOLDER, f))]
    print(f"Found {len(files)} files. Processing...")

    count = 0
    for file_name in files:
        file_path = os.path.join(DOCS_FOLDER, file_name)
        file_ext = os.path.splitext(file_name)[1].lower()
        
        loader = None
        
        try:
            # --- SELECT THE CORRECT LOADER ---
            if file_ext == ".pdf":
                loader = PyPDFLoader(file_path)
            elif file_ext == ".docx":
                loader = Docx2txtLoader(file_path)
            elif file_ext == ".doc":
                loader = UnstructuredWordDocumentLoader(file_path)
            elif file_ext == ".txt" or file_ext == ".md":
                loader = TextLoader(file_path, encoding="utf-8")
            else:
                print(f"SKIPPING: {file_name} (Unsupported format: {file_ext})")
                continue

            print(f"--> Processing: {file_name}")
            raw_docs = loader.load()
            
            # Split text into chunks
            chunks = text_splitter.split_documents(raw_docs)
            
            # Add to Database
            if chunks:
                vectorstore.add_documents(chunks)
                print(f"    Saved {len(chunks)} chunks.")
                count += 1
            else:
                print(f"    WARNING: {file_name} was empty or couldn't be read.")

        except Exception as e:
            print(f"ERROR processing {file_name}: {e}")

    print(f"\n--- SUCCESS: Processed {count} files. Database saved at '{DB_PATH}' ---")

if __name__ == "__main__":
    # Optional: Uncomment the next line if you want to WIPE the database clean every time you run this
    # if os.path.exists(DB_PATH): shutil.rmtree(DB_PATH)
    
    load_documents()