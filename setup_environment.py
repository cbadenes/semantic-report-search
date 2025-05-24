# This script prepares the environment for the NLP course.
# It pre-downloads word embeddings for Flair and installs the spaCy English model.
print(f"Downloading NLTK packages...")
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# Pre-download Flair word embeddings
from flair.embeddings import WordEmbeddings
import subprocess
embeddings_to_download = ["en-glove", "en"]

for emb in embeddings_to_download:
    print(f"Downloading Flair embedding: '{emb}'...")
    _ = WordEmbeddings(emb)
    print(f"'{emb}' downloaded and cached.\n")

# Download spaCy small English model
print("Downloading spaCy English model 'en_core_web_sm'...")
subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"], check=True)
print("spaCy model downloaded.")
