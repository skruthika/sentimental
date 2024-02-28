import streamlit as st
from transformers import pipeline, set_seed


# Load sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

def main():
    st.title("Sentiment Analysis")

    # User input for text
    text = st.text_area("Enter text for sentiment analysis:")

    if st.button("Analyze Sentiment"):
        if text:
            # Analyze sentiment
            result = sentiment_analyzer(text)

            # Display result
            st.write(f"Sentiment: {result[0]['label']}")
            st.write(f"Confidence: {result[0]['score']:.2f}")
        else:
            st.warning("Please enter some text for analysis.")

if __name__ == "__main__":
    main()
