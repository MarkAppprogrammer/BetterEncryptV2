from huggingface_hub import InferenceClient
from .passwordgen import numbers
import os
import re
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None

try:
    import requests
except Exception:
    requests = None

try:
    import language_tool_python
except Exception:
    language_tool_python = None

safe = False
""" numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def contains(inputString, blackList):
    blackList = set(blackList)
    for char in inputString: 
        if char in blackList:
            return True
    return False """


""" #implement in django view
while not safe:
    prompt = input("What would you use the password for? ")

    # possibly check for all non-alpabetical chars
    for char in prompt:
        if char.isalpha():
            safe = True
        else:
            safe = False """

def process_data(prompt):
    prompt = prompt.lower()
    prompt = "Generate a password for my " + prompt
    #grammer /punc check
    correct_prompt = prompt
    if language_tool_python is not None:
        tool = language_tool_python.LanguageTool("en-US")
        correct_prompt = tool.correct(prompt)

    #api for model
    token = os.environ.get("HF_TOKEN")
    if not token and load_dotenv is not None:
        try:
            from django.conf import settings

            load_dotenv(Path(settings.BASE_DIR) / ".env")
            token = os.environ.get("HF_TOKEN")
        except Exception:
            token = os.environ.get("HF_TOKEN")
    if not token:
        raise RuntimeError("Missing HF_TOKEN environment variable for Hugging Face inference.")
    client = InferenceClient(
        "microsoft/Phi-3-mini-4k-instruct",
        token=token,
    )

    final = ""
    try:
        for message in client.chat_completion(
            messages=[
                {
                    "role": "system",
                    "content": "You will be given a prompt that details a password’s use. Provide two numbers, the first number will detail the security level required, and the second number will detail the level of memorability required. Both numbers are rated on a scale from 01 - 10 where 1 is the lowest level and is the highest. Provide the security level number first and the other number second without explanations.",
                },
                {"role": "user", "content": correct_prompt},
            ],
            max_tokens=100,
            stream=True,
        ):
            final += message.choices[0].delta.content
        return parse_result(final)
    except Exception:
        # If the inference call is blocked/unavailable (proxy/network), fall back
        # to reasonable defaults so the site remains usable.
        return ["7", "5"]
    
def parse_result(data):
    print(data)
    nums = re.findall(r"\d+", str(data))
    if len(nums) >= 2:
        return [nums[0], nums[1]]
    if len(nums) == 1:
        return [nums[0], ""]
    return ["", ""]
