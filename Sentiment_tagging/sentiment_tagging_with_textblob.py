import os
from textblob import TextBlob
import pandas as pd


SOURCE_PATH=os.path.join("Sentiment_tagging","news_articles_source_file.xlsx")
DESTINATION_PATH=os.path.join("Sentiment_tagging","new_articles_with_sentiment_TextBlob.xlsx")
# Function to determine sentiment
def determine_sentiment(text):
    # Create a TextBlob object
    analysis = TextBlob(text)
    # Use TextBlob's sentiment polarity
    polarity = analysis.sentiment.polarity
    # Determine sentiment
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Load the dataset
source_file_path =  SOURCE_PATH
df = pd.read_excel(source_file_path)

# Apply sentiment analysis
df['text_sentiment'] = df['text'].apply(determine_sentiment)
df['ctext_sentiment'] = df['ctext'].apply(determine_sentiment)

# Save the results to a new Excel file
destination_file_path = DESTINATION_PATH
df.to_excel(destination_file_path, index=False)

print("Sentiment analysis completed and the result is saved to the new Excel file.")
