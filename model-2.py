# model-2.py

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report

# Load the CSV files
data1 = pd.read_csv('IndianElection19TwitterData.csv')
data2 = pd.read_csv('RahulRelatedTweetsWithSentiment.csv')
data3 = pd.read_csv('ModiRelatedTweetsWithSentiment.csv')

# Combine labeled datasets for training
labeled_data = pd.concat([data2[['Tweet', 'Emotion']], data3[['Tweet', 'Emotion']]], ignore_index=True)

# Clean the data by removing null or empty tweets and labels
labeled_data = labeled_data.dropna(subset=['Tweet', 'Emotion'])
labeled_data = labeled_data[labeled_data['Tweet'].str.strip().astype(bool)]

# Split data into training and test sets
X = labeled_data['Tweet']
y = labeled_data['Emotion']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a pipeline for text vectorization and model training
model_pipeline = make_pipeline(CountVectorizer(), MultinomialNB())

# Train the model
model_pipeline.fit(X_train, y_train)

# Evaluate the model
y_pred = model_pipeline.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Function to predict sentiment for a given candidate's name and determine election prediction
def analyze_sentiment_for_candidate(candidate_name, data_frame, model):
    candidate_tweets = data_frame[data_frame['Tweet'].str.contains(candidate_name, case=False, na=False)]
    if candidate_tweets.empty:
        print(f"No tweets found for candidate '{candidate_name}'.")
        return
    predictions = model.predict(candidate_tweets['Tweet'])
    positive_count = (predictions == 'pos').sum()
    negative_count = (predictions == 'neg').sum()

    # Display the sentiment analysis results
    print(f"Sentiment analysis for '{candidate_name}':")
    print(f"Positive: {positive_count}")
    print(f"Negative: {negative_count}")

    # Basic logic for predicting the election outcome
    if positive_count > negative_count:
        print(f"Based on the sentiment analysis, '{candidate_name}' is likely to have a favorable outcome in the next election.")
    else:
        print(f"Based on the sentiment analysis, '{candidate_name}' might face challenges in the next election.")

# Get candidate name from the terminal
candidate_name = input("Enter the candidate name for sentiment analysis: ")
analyze_sentiment_for_candidate(candidate_name, data1, model_pipeline)

