from core.config import client

def getGPTAnswer(prompt: str, task_text: str) -> str:
    messages = [{"role": "system", "content": prompt}]
    messages += [{"role": "user", "content": task_text}]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
    return response.choices[0].message.content
