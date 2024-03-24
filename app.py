from flask import Flask, render_template, request
import pickle

app = Flask(__name__, static_url_path='/static', static_folder='static')

# Load the trained model and TF-IDF vectorizer
with open('model/model.pkl', 'rb') as f:
    model, tfidf_vectorizer = pickle.load(f)

def preprocess_text(text):
    return text

def predict_sentiment(text):
    text_processed = preprocess_text(text)
    text_vectorized = tfidf_vectorizer.transform([text_processed])
    prediction = model.predict(text_vectorized)[0]
    sentiment = 'Positive' if prediction == 1 else 'Negative'
    return sentiment

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.form['text']
        sentiment = predict_sentiment(text)
        return render_template('result.html', text=text, sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)
