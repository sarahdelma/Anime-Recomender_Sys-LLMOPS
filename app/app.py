import streamlit as st
from dotenv import load_dotenv
import sys
import os

# Ensure project root is in Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pipeline.pipeline import AnimeRecommendationPipeline

# Page config
st.set_page_config(
    page_title="Anime Recomender",
    layout="wide"
)

# Load environment variables
load_dotenv()

# Initialize pipeline once (Streamlit 1.25+)
@st.cache_resource(show_spinner=False)
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

# UI
st.title("Anime Recomender System")

query = st.text_input(
    "Describe the type of anime you like",
    placeholder="Example: light‑hearted anime with school setting"
)

if query:
    with st.spinner("Fetching recommendations..."):
        try:
            response = pipeline.recommend(query)
            st.subheader("Recommendations")
            st.write(response)
        except Exception as e:
            st.error(f"Something went wrong: {e}")
