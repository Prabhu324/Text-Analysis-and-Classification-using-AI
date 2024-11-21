# app.py
from flask import Flask, render_template, jsonify
import joblib

import os

template_dir = os.path.abspath('templates')
app = Flask(__name__, template_folder=template_dir)

# Load the trained model and vectorizer
model = joblib.load('svm_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Load the articles and their categories
articles = []
with open('formatted_articles.txt', 'r', encoding='utf-8') as f:  # Ensure to read with UTF-8 encoding
    for line in f:
        line = line.strip()
        if line:  # Check if the line is not empty
            parts = line.split('\t')
            if len(parts) == 2:  # Ensure there are exactly two parts
                category, article = parts
                try:
                    # Attempt to convert category to an integer
                    articles.append((int(category), article))
                except ValueError as e:
                    print(f"Skipping line due to error: {e} | Line content: {line}")

# Create a mapping from target indices to category names
target_names = ['alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware',
                'comp.sys.mac.hardware', 'comp.windows.x', 'misc.forsale', 'rec.autos', 'rec.motorcycles',
                'rec.sport.baseball', 'rec.sport.hockey', 'sci.crypt', 'sci.electronics', 'sci.med',
                'sci.space', 'soc.religion.christian', 'talk.politics.guns', 'talk.politics.mideast',
                'talk.politics.misc', 'talk.religion.misc']

@app.route('/')
def index():
    return render_template('index.html', categories=target_names)

@app.route('/articles/<category>')
def get_articles(category):
    # Find the index of the category
    category_index = target_names.index(category)
    
    # Get the articles that belong to this category
    filtered_articles = [{'title': f'Article {i+1}', 'link': f'#', 'content': article} 
                         for i, (cat, article) in enumerate(articles) if cat == category_index]
    
    return jsonify(filtered_articles)

if __name__ == '__main__':
    app.run(debug=True)
