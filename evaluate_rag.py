import os
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevance, context_precision

def run_batch_evaluation():
    print("Initializing RAGAS Batch Evaluation...")
    
    # Sample test dataset
    data = {
        "question": ["What is the main objective of the system?"],
        "answer": ["The system evaluates RAG pipeline performance using metrics like faithfulness and answer relevance."],
        "contexts": [["RAGAS is a framework for evaluating Retrieval Augmented Generation systems."]],
        "ground_truth": ["The objective is to evaluate RAG pipelines using RAGAS metrics."]
    }
    
    dataset = Dataset.from_dict(data)
    
    # Note: Requires OPENAI_API_KEY set in environment
    if "OPENAI_API_KEY" in os.environ:
        result = evaluate(dataset, metrics=[faithfulness, answer_relevance, context_precision])
        print("Evaluation Results:", result)
    else:
        print("OPENAI_API_KEY not found. Skipping live API call.")

if __name__ == "__main__":
    run_batch_evaluation()
