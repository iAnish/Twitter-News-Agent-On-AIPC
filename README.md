# AIPC Autonomous News Agent
An autonomous, edge-based AI agent that crawls curated news sources, extracts key insights, and generates viral social media content—all running locally on Intel Core Ultra hardware.

# 🌟 Overview
This project demonstrates the power of Edge AI. Instead of relying on expensive cloud APIs, this agent utilizes the Intel NPU (Neural Processing Unit) and iGPU to handle LLM inference locally. It ensures data privacy, reduces latency, and leverages the latest in OpenVINO™ optimization.

# Key Features
Local Inference: Powered by Qwen2.5-1.5B-Instruct optimized for Intel NPU.

Hardware Selection: Toggle between NPU (for power efficiency) and iGPU (for throughput).Smart Crawling: Uses DuckDuckGo News and RSS feeds to gather real-time context. Assuming you have a brand new AIPC, here is the steps to get an complete AI Agent to generate tweets on your topics of interest.

Automated Scheduling: Built-in background worker to generate drafts every morning.Open Source Stack: 100% transparent tools—no proprietary "black boxes."

# 🛠️ Tech StackComponentTechnology
Model Qwen2.5-1.5B (INT4 Quantized)Inference Engine
OpenVINO™ GenAISearch/Crawlduckduckgo-search & newspaper4kUI Framework
Streamlit Orchestration AP
Scheduler Social APITweepy (Twitter/X v2 API)

# 🚀 Getting . Prerequisites
An Intel Core Ultra processor (Lunar Lake, Meteor Lake, etc.).Intel NPU Drivers installed.Python 3.10 or 3.11.2. 
Installation
# Clone the repo
git clone https://github.com/iAnish/Twitter-News-Agent-On-AIPC.git 
cd aipc-news-agent






# Step 1: Install conda for Windows using Miniconda installer
https://docs.conda.io/projects/conda/en/stable/user-guide/install/windows.html


# Step 2:  Create a clean environment
conda create -n ai-agent python=3.10 -y

# Step 3: Activate the environment
conda activate ai-agent


# Step 4: Install OpenVINO and dependencies
pip install openvino-genai huggingface_hub newspaper4k streamlit fastapi transformers==4.45.0 openvino-tokenizers googlesearch-python duckduckgo-search


# Step 5: Convert the model
optimum-cli export openvino --model Qwen/Qwen2.5-1.5B-Instruct --task text-generation-with-past --weight-format int4 --library transformers ./qwen_ov_int4

# Step 6: Clone this repo
git clone https://github.com/iAnish/Twitter-News-Agent-On-AIPC.git

# Step 7: Run the streamlit app
streamlit run app.py

# Pre-install Checks
Driver Check: Ensure you have the latest Intel NPU Driver installed from the Intel website.

# Hardware Monitoring: 
Open your Task Manager (Windows) or intel-gpu-tools (Linux). You will see the NPU usage spike when the tweet is being generated, leaving your CPU and GPU free for other tasks.

# Pro-Tips for AIPC
NPU for Power: If you are running on battery, keep the device on NPU. It is significantly more energy-efficient than the iGPU.

Static Shapes: For the NPU, ensure your model is compiled with static input shapes if you encounter latency issues; however, the openvino-genai pipeline handles most of this automatically in the 2025+ versions.

![alt text](https://github.com/iAnish/Twitter-News-Agent-On-AIPC/blob/main/IMG_4960.JPG)





