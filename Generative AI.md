A very important info before using RAG
# Making RAG better by contextual retrieval
https://www.anthropic.com/news/contextual-retrieval
    Introducing Contextual Retrieval --- Better than RAG -- actually uses hybrid search(embedding search+word search)

A note on simply using a longer prompt
Sometimes the simplest solution is the best. If your knowledge base is smaller than 200,000 tokens (about 500 pages of material), you can just include the entire knowledge base in the prompt that you give the model, with no need for RAG or similar methods.

A few weeks ago, we released prompt caching for Claude, which makes this approach significantly faster and more cost-effective. Developers can now cache frequently used prompts between API calls, reducing latency by > 2x and costs by up to 90% (you can see how it works by reading our prompt caching cookbook).

![image](https://github.com/user-attachments/assets/71c06d83-a238-44c2-b73d-6ae6e994ad93)

### Building a contextual RAG system
 https://colab.research.google.com/drive/1Yk3KgQRM9s2lSEwV2w9LUkeFD_RksTK7?usp=sharing 
--------

## Chunking Strategies for LLM Applications - 
https://www.pinecone.io/learn/chunking-strategies/
------------------------------
