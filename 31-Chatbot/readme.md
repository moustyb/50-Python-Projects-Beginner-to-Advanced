# 🤖 NLP Chatbot — Advanced Project

A fully‑featured Natural Language Processing (NLP) chatbot built with machine learning, intent classification, and text processing.  
This project demonstrates how to build a real conversational AI system using Python, spaCy, NLTK, and scikit‑learn.

---

## 🚀 Features

- ✅ Intent classification using ML (TF‑IDF + Logistic Regression / SVM)  
- ✅ NLP preprocessing (tokenization, lemmatization, stopword removal)  
- ✅ Entity extraction using spaCy  
- ✅ JSON‑based training dataset  
- ✅ Confidence‑based fallback responses  
- ✅ Modular architecture (utils, model, data)  
- ✅ Trainable model (`train_intents.py`)  
- ✅ Interactive chatbot (`main.py`)  

---

## 📁 Project Structure

```
chatbot_project/
│
├── main.py                     # Runs the chatbot and handles conversation flow
├── train_intents.py            # Trains the intent classification model
│
├── model/
│     ├── intent_model.pkl      # Saved ML model for intent prediction
│     └── vectorizer.pkl        # TF‑IDF vectorizer used during training
│
├── data/
│     └── intents.json          # Training data: patterns, tags, responses
│
├── utils/
│     ├── nlp_utils.py          # Tokenization, preprocessing, entity extraction
│     └── response_utils.py     # Response selection, fallback logic
│
└── requirements.txt            # Python dependencies
```

---

## 📦 Installation

1. Clone the project:

```
git clone https://github.com/yourusername/chatbot_project.git
cd chatbot_project
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Download spaCy language model:

```
python -m spacy download en_core_web_sm
```

---

## 🧠 Training the Model

Before running the chatbot, train the intent classifier:

```
python train_intents.py
```

This will:

- Load `data/intents.json`
- Vectorize training text
- Train the ML model
- Save:
  - `model/intent_model.pkl`
  - `model/vectorizer.pkl`

---

## 💬 Running the Chatbot

After training:

```
python main.py
```

You’ll enter an interactive chat loop where the bot predicts intents and responds accordingly.

---

## 📝 intents.json Format

Your training data lives in:

```
data/intents.json
```

Example structure:

```
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": ["hello", "hi", "hey"],
      "responses": ["Hello!", "Hi there!", "How can I help you today?"]
    }
  ]
}
```

You can expand this file to teach the chatbot new skills.

---

## 🧩 How It Works

### **1. Preprocessing**
- Tokenization  
- Lowercasing  
- Lemmatization  
- Stopword removal  

### **2. Vectorization**
- TF‑IDF converts text into numerical features.

### **3. Intent Classification**
- Logistic Regression or SVM predicts the user’s intent.

### **4. Response Selection**
- Bot selects a response from `intents.json`  
- If confidence is low → fallback response

### **5. Entity Extraction**
- spaCy extracts:
  - names  
  - dates  
  - locations  
  - numbers  

---

## 🔮 Future Improvements

- Add BERT‑based intent classification  
- Add memory / context tracking  
- Add sentiment analysis  
- Add a Flask web UI  
- Add voice input/output  
- Add multilingual support  

---

## ✅ Summary

This project is a complete, modular, and scalable NLP chatbot system.  
It’s the perfect foundation for building:

- Customer support bots  
- FAQ assistants  
- Voice assistants  
- AI companions  
- Domain‑specific chatbots  
