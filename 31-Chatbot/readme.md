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
