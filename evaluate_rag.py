import os
import asyncio
import nest_asyncio

# Apply nest_asyncio to fix event loop conflicts in Streamlit
nest_asyncio.apply()

from datasets import Dataset
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision
)
from langchain_openai import ChatOpenAI

def run_batch_evaluation(queries=None, responses=None, contexts=None, ground_truths=None):
    print("Initializing RAGAS Batch Evaluation...")
    
    if queries is None:
        queries = ["What is the capital of France?"]
        responses = ["Paris is the capital of France."]
        contexts = [["Paris is the major city and capital of France."]]
        ground_truths = ["Paris"]

    data = {
        "question": queries,
        "answer": responses,
        "contexts": contexts,
        "ground_truth": ground_truths
    }
    
    dataset = Dataset.from_dict(data)
    
    # Explicitly define the evaluation LLM
    eval_llm = ChatOpenAI(model="gpt-4o")
    
    # Run RAGAS evaluation
    score = evaluate(
        dataset=dataset,
        metrics=[
            faithfulness,
            answer_relevancy,
            context_precision
        ],
        llm=eval_llm
    )
    
    return score

if __name__ == "__main__":
    result = run_batch_evaluation()
    print("Evaluation Results:", result)