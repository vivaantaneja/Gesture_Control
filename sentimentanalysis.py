from textblob import TextBlob

def get_sentiment(sentence):
    # Create a TextBlob object with the input sentence
    blob = TextBlob(sentence)
    
    # Get the polarity score of the sentence (-1 to 1)
    polarity = blob.sentiment.polarity
    
    # Classify the sentiment as positive, negative or neutral based on the polarity score
    if polarity > 0:
        sentiment = 'positive'
    elif polarity < 0:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    
    return sentiment

# Example usage:
sentence = input('Emter your remarks')
sentiment = get_sentiment(sentence)
print(sentiment)


