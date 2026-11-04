
import asyncio

from datasets import Dataset
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision
)
from langchain_openai import ChatOpenAI


async def run_batch_evaluation_async(
    queries=None,
    responses=None,
    contexts=None,
    ground_truths=None
):
    print("Initializing RAGAS Batch Evaluation...")

    if queries is None:
        queries = ["What is the capital of France?"]
        responses = ["Paris is the capital of France."]
        contexts = [
            ["Paris is the major city and capital of France."]
        ]
        ground_truths = ["Paris"]

    data = {
        "question": queries,
        "answer": responses,
        "contexts": contexts,
        "ground_truth": ground_truths
    }

    dataset = Dataset.from_dict(data)

    eval_llm = ChatOpenAI(model="gpt-4o")

    # Run RAGAS evaluation
    score = await evaluate(
        dataset=dataset,
        metrics=[
            faithfulness,
            answer_relevancy,
            context_precision
        ],
        llm=eval_llm
    )

    return score


def run_batch_evaluation(
    queries=None,
    responses=None,
    contexts=None,
    ground_truths=None
):
    """
    Synchronous entry point.
    Use run_batch_evaluation_async() inside an existing async event loop.
    """

    try:
        asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.run(
            run_batch_evaluation_async(
                queries,
                responses,
                contexts,
                ground_truths
            )
        )

    raise RuntimeError(
        "An event loop is already running. "
        "Use 'await run_batch_evaluation_async()' instead."
    )


if __name__ == "__main__":
    result = run_batch_evaluation()
    print("Evaluation Results:", result)
