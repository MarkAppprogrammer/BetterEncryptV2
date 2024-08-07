from huggingface_hub import InferenceClient
import language_tool_python
from .passwordgen import numbers

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

    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(prompt)
    correct_prompt = tool.correct(prompt)
    print(correct_prompt)

    #api for model
    client = InferenceClient(
        "microsoft/Phi-3-mini-4k-instruct",
        token="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",
    )

    final = ""

    for message in client.chat_completion(
        messages = [
            {
                "role": "system",
                "content": "You will be given a prompt that details a password’s use. Provide two numbers, the first number will detail the security level required, and the second number will detail the level of memorability required. Both numbers are rated on a scale from 01 - 10 where 1 is the lowest level and is the highest. Provide the security level number first and the other number second without explanations."
            },
            {
                "role": "user",
                "content": correct_prompt
            }
        ],
        max_tokens=100,
        stream=True,
    ):
        final += message.choices[0].delta.content
    return parse_result(final)
    
def parse_result(data):
    print(data)
    final = ["", ""]

    data = str(data)

    check = 0
    for i, char in enumerate(data):
        if char in numbers:
            if check == 0:
                final[check] += char
                if data[i + 1] in numbers:
                    final[check] += char
                check += 1
            else:
                final[check] += char
                if i != len(data) - 1:
                    if data[i + 1] in numbers:
                        final[check] += char
                break

    return final
