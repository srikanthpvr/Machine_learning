A very important info before using RAG
# Making RAG better by contextual retrieval
https://www.anthropic.com/news/contextual-retrieval
    Introducing Contextual Retrieval --- Better than RAG -- actually uses hybrid search(embedding search+word search)

A note on simply using a longer prompt
Sometimes the simplest solution is the best. If your knowledge base is smaller than 200,000 tokens (about 500 pages of material), you can just include the entire knowledge base in the prompt that you give the model, with no need for RAG or similar methods.

A few weeks ago, we released prompt caching for Claude, which makes this approach significantly faster and more cost-effective. Developers can now cache frequently used prompts between API calls, reducing latency by > 2x and costs by up to 90% (you can see how it works by reading our prompt caching cookbook).

--------

## Chunking Strategies for LLM Applications - 
https://www.pinecone.io/learn/chunking-strategies/
------------------------------
