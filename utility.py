import os
import base64
from langchain_groq import ChatGroq
from langchain_core.output_parsers.string import StrOutputParser

def format_data_for_ai(diffs, commit_messages):
    prompt = None
    # Combine the changes into a string with clear delineation.
    changes = '\n'.join([
        f'File: {file["filename"]}\\Diff: {file["patch"]}\n' 
        for file in diffs
    ])
    # Combine all commit messages
    commit_messages = '\n'.join(commit_messages) + '\n\n'

    # Construct the prompt with clear instructions for the LLM.
    prompt = (
        "Please review the following code changes and commit messages from a GitHub pull request:\n"
        "Code changes from Pull Request:\n"
        f"{changes}\n"
        "Commit messages:\n"
        f"{commit_messages}"
        "Consider the code changes and commit messages and provide a summary of the changes.\n"
        "Finally, highlight any potential issues with the code changes.\n"
    )

    return prompt

def call_ai(prompt):
    client = ChatGroq(api_key=os.getenv('GROQ_API_KEY'), model="llama3-70b-8192")

    try:
        messages = [
            {"role": "system", "content": "You are an AI expert software engineer, trained to review PRs. Your main goals are to summarize the changes, and highlight any potential issues."},
            {"role": "user", "content": prompt}
        ]

        response = client.invoke(input=messages)
        parser = StrOutputParser()
        content = parser.invoke(input=response)

        return content
    except Exception as e:
        print(f"Error making LLM call: {e}")
