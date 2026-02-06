import streamlit as st
from agent import TweetAgent

st.set_page_config(page_title="Intel AIPC Tweet Agent", layout="wide")

st.title("Intel Core Ultra AIPC AI Agent")
st.sidebar.header("Hardware Settings")

# Option to select NPU or iGPU
target_device = st.sidebar.selectbox("Inference Device", ["GPU", "NPU"])
topic = st.text_input("Topic of Interest", "Open Source AI")

if st.button("Generate Latest Tweet"):
    with st.spinner(f"Crawling news and running inference on {target_device}..."):
        agent = TweetAgent(device=target_device)
        tweet = agent.generate_tweet(topic)
        st.success("Generated Tweet:")
        st.write(f"> {tweet}")

st.info("Note: NPU is optimized for low power; iGPU (GPU) offers higher throughput.")
