# Twitter-News-Agent-On-AIPC
A news agent that crawls the web to search for information about a particular user defined keyword and creates a tweet. Uses the Qwen2.5-1.5B-Instruct LLM Model


Assuming you have a brand new AIPC, here is the steps to get an complete AI Agent to generate tweets on your topics of interest.

Step 1: 
# Install conda for Windows using Miniconda installer
https://docs.conda.io/projects/conda/en/stable/user-guide/install/windows.html

Step 2: 
# Create a clean environment
conda create -n ai-agent python=3.10 -y

Step 3: conda activate ai-agent

Step 4: 
# Install OpenVINO and dependencies
pip install openvino-genai huggingface_hub newspaper4k streamlit fastapi transformers==4.45.0 openvino-tokenizers googlesearch-python duckduckgo-search

Step 4: 
# Convert the model
optimum-cli export openvino --model Qwen/Qwen2.5-1.5B-Instruct --task text-generation-with-past --weight-format int4 --library transformers ./qwen_ov_int4

