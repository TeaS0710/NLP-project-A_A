import json
import glob

def create_corpus():
    """Crée un corpus JSON simple"""
    corpus = {
        "metadata": {
            "name": "Corpus exemple",
            "language": "fr",
            "documents_count": 0
        },
        "documents": []
    }
    return corpus

def add_document(corpus, doc_id, title, text):
    """Ajoute un document au corpus"""
    document = {
        "id": doc_id,
        "title": title,
        "text": text,
        "metadata": {
            "word_count": len(text.split()),
            "char_count": len(text)
        }
    }
    corpus["documents"].append(document)
    corpus["metadata"]["documents_count"] += 1

def save_corpus(corpus, filename):
    """Sauvegarde le corpus en JSON"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(corpus, f, ensure_ascii=False, indent=2)

def load_texts_from_files(pattern="*.txt"):
    """Charge des textes depuis des fichiers"""
    texts = []
    for filepath in glob.glob(pattern):
        with open(filepath, 'r', encoding='utf-8') as f:
            texts.append((filepath, f.read()))
    return texts

# Exemple d'utilisation
if __name__ == "__main__":
    # Créer le corpus
    corpus = create_corpus()

    # Ajouter des documents exemples
    add_document(corpus, "doc_1", "Premier document", "premier document")
    add_document(corpus, "doc_2", "Deuxième document", "deuxième document")

    # Sauvegarder
    save_corpus(corpus, "corpus_simple.json")
