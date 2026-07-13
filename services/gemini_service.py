# import os
# from google import genai
# # import google.generativeai as genai
# from dotenv import load_dotenv
# load_dotenv()

# # genai.configure(
# #     api_key=os.getenv("GEMINI_API_KEY")
# # )
# client=genai.Client(
#     api_key=os.getenv("GEMINI_API_KEY")
# )
# # model = genai.GenerativeModel("gemini-2.5-flash")


# def ask_gemini(question, context):

#     prompt = f"""
# You are an Industrial Engineering AI Assistant.

# Answer ONLY using the provided context.

# If the answer is not present in the context, reply:

# "I could not find this information in the uploaded documents."

# -----------------------
# Context:

# {context}

# -----------------------

# Question:

# {question}

# Answer:
# """

#     response = client.models.generate_content(
#         model="gemini-2.5-flash",
#         contents=prompt,
#     )

#     return response.text


import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_gemini(question: str, context: str):

    prompt = f"""
You are an Industrial AI Assistant.

Answer ONLY from the given context.

If the answer is not present in the context, reply:
"I could not find this information in the uploaded documents."

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text