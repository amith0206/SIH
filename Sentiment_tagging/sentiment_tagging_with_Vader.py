import os
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd

SOURCE_PATH=os.path.join("Sentiment_tagging","news_articles_source_file.xlsx")
DESTINATION_PATH=os.path.join("Sentiment_tagging","new_articles_with_sentiment_Vader.xlsx")
# Download the VADER lexicon
nltk.download('vader_lexicon')

# Initialize the VADER sentiment intensity analyzer
sia = SentimentIntensityAnalyzer()

# Function to determine sentiment
def determine_sentiment(text):
    # Obtain the polarity scores for the text
    sentiment_score = sia.polarity_scores(text)['compound']
    # Determine sentiment based on the compound score
    if sentiment_score > 0.05:
        return 'Positive'
    elif sentiment_score < -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Load the dataset from the specified source path
source_file_path = SOURCE_PATH
df = pd.read_excel(source_file_path)

# Apply sentiment analysis to the 'text' and 'ctext' columns
df['text_sentiment'] = df['text'].apply(determine_sentiment)
df['ctext_sentiment'] = df['ctext'].apply(determine_sentiment)

# Save the DataFrame with the new sentiment columns to the specified destination path
destination_file_path = DESTINATION_PATH
df.to_excel(destination_file_path, index=False)

print("Sentiment analysis completed and the result is saved to the new Excel file.")
