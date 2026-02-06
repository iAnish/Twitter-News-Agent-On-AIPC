import openvino_genai as ov_genai
from duckduckgo_search import DDGS
from newspaper import Article

class TweetAgent:
    def __init__(self, device="NPU"):
        # device can be "NPU" or "GPU" (for iGPU)
        self.pipe = ov_genai.LLMPipeline("./qwen_ov_int4", device)
        
    def crawl_news(self, topic):
        context = ""
        # DDGS is more reliable and has a specific news search
        with DDGS() as ddgs:
            # Get the top 3 news results
            results = list(ddgs.news(topic, max_results=3))
            
        for r in results:
            try:
                # newspaper4k extracts the actual body text from the URL
                article = Article(r['url'])
                article.download()
                article.parse()
                
                context += f"\n--- NEWS SOURCE: {r['title']} ---\n"
                context += f"DATE: {r.get('date', 'N/A')}\n"
                context += f"CONTENT: {article.text[:600]}...\n" # Limit text to stay in context window
            except Exception as e:
                print(f"Skipping {r['url']} due to error: {e}")
                continue
                
        return context if context else "No recent news found."

    def generate_tweet(self, topic):
        news_context = self.crawl_news(topic)
       
        
        # Crafting the prompt for Qwen2.5-1.5B
        prompt = (
            f"<|im_start|>system\nYou are a tech-savvy social media manager.<|im_end|>\n"
            f"<|im_start|>user\nUsing the following news context, write a punchy, professional tweet "
            f"about {topic}. Include 210 relevant hashtags.\n\n"
            f"CONTEXT:\n{news_context}<|im_end|>\n"
            f"<|im_start|>assistant\n"
        )
        
        # OpenVINO GenAI inference on Intel NPU/iGPU
        config = ov_genai.GenerationConfig(
           max_new_tokens=200,
           do_sample=True,
           temperature=0.7,
           top_p=0.95
           )
        
        print(prompt)


        result = self.pipe.generate(prompt, config)
        return result
