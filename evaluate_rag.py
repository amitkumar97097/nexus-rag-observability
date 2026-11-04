import os
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision
)

def run_batch_evaluation(queries=None, responses=None, contexts=None, ground_truths=None):
    print("Initializing RAGAS Batch Evaluation...")
    
    # Sample evaluation dataset structure if none provided
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
    
    # Run RAGAS evaluation using updated metric names
    score = evaluate(
        dataset=dataset,
        metrics=[
            faithfulness,
            answer_relevancy,
            context_precision
        ]
    )
    
    return score

if __name__ == "__main__":
    result = run_batch_evaluation()
    print("Evaluation Results:", result)