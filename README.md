# Twitter-News-Agent-On-AIPC
A news agent that crawls the web to search for information about a particular user defined keyword and creates a tweet. Uses the Qwen2.5-1.5B-Instruct LLM Model


Assuming you have a brand new AIPC, here is the steps to get an complete AI Agent to generate tweets on your topics of interest.


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




