from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from src.prompt_template import get_anime_prompt


class AnimeRecommender:
    def __init__(self, retriever, api_key: str, model_name: str):
        # Initialize LLM
        self.llm = ChatGroq(
            api_key=api_key,
            model=model_name,
            temperature=0
        )

        # Load prompt
        self.prompt = get_anime_prompt()

        # Build LCEL retrieval pipeline
        self.chain = (
            RunnableParallel(
                context=retriever,
                question=RunnablePassthrough()
            )
            | self.prompt
            | self.llm
        )

    def get_recommendation(self, query: str) -> str:
        response = self.chain.invoke(query)
        return response.content
