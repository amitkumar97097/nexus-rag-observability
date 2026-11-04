import os
import asyncio
import nest_asyncio

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
    
    # Ensure there is a running event loop for asyncio tasks in Python 3.14
    try:
        loop = asyncio.get_event_loop()
        if loop.is_closed():
            raise RuntimeError()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

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
    eval_llm = ChatOpenAI(model="gpt-4o")
    
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