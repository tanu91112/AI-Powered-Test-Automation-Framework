from transformers import pipeline

generator = pipeline(
    task="text2text-generation",
    model="google/flan-t5-base",
    device=-1   # CPU
)
def generate_with_flan(prompt):

    result = generator(
        prompt,
        max_new_tokens=256,
        do_sample=False,
        repetition_penalty=1.5
    )

    return result[0]["generated_text"]