# Text Analysis and Classification Using AI  

This project implements a machine learning pipeline to classify text articles from the 20 Newsgroups dataset into predefined categories. It preprocesses data, evaluates multiple classification models, and deploys the best-performing model in a web application.  

## Features  
- Preprocessing of textual data (lowercasing, punctuation removal, stopword filtering).  
- Model training and evaluation with Naive Bayes, Logistic Regression, and Support Vector Machine (SVM).  
- Deployment of the SVM model using Flask.  
- A user-friendly web application with dynamic article display based on selected categories.  

## Dataset  
The project utilizes the **20 Newsgroups** dataset from the `sklearn.datasets` module, which includes diverse topics for classification.  

## Methodology  
### 1. Data Preprocessing  
- Lowercased all text for uniformity.  
- Removed punctuation and stopwords using `NLTK`.  

### 2. Model Training and Evaluation  
- Models: Naive Bayes, Logistic Regression, Support Vector Machine (SVM).  
- The SVM model achieved the highest accuracy (91%).  

### 3. Deployment  
- The trained SVM model and TF-IDF vectorizer were saved using `joblib`.  
- Developed a **Flask web application** to display classified articles.  

## Web Application  
The web application includes:  
- **Homepage**: Lists available categories.  
- **Dynamic Content**: Fetches and displays articles based on selected categories.  
- **Frontend**: Built with HTML and JavaScript for an interactive user experience.  

## Model Evaluation  
- **Accuracy**: SVM achieved 91%.  
- Detailed classification report and confusion matrix are included in the project files.  

## Technologies Used  
- Python (Scikit-learn, NLTK, Flask, joblib)  
- HTML, JavaScript  


