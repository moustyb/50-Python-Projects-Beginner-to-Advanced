import os
import sys
import joblib

MODEL_PATH = "sentiment_model.joblib"

def load_model():
    if not os.path.exists(MODEL_PATH):
        print("Model not found. You must have a trained model named sentiment_model.joblib.")
        sys.exit(1)
    return joblib.load(MODEL_PATH)

def main():
    if len(sys.argv) < 2:
        print("Usage: python predict.py \"your text here\"")
        sys.exit(1)

    text = " ".join(sys.argv[1:])
    model = load_model()
    prediction = model.predict([text])[0]

    print(f"Text: {text}")
    print(f"Predicted sentiment: {prediction}")

if __name__ == "__main__":
    main()
