from flask import Flask, render_template, request, jsonify
import os
from groq import Groq
# from dotenv import load_dotenv

# load_dotenv()

app = Flask(__name__)

message_history=[]

client = Groq(
    api_key="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"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    # Converting the post request user-input from JSON(initial) to text
    user_message = request.json.get('message')
    return ques_gen(user_message)

def ques_gen(user_message):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system","content":"You are an expert in study abroad services help the user for the same. Ask the user for detailes like the country they want to go to the college they prefer and the course they want to pursue. Ask these questions one by one and in conversational form"
            },
            {   
                "role": "user","content": user_message,
            }
        ],
        model="llama3-8b-8192",
    )
    
    # response_message = chat_completion.choices[0].message.content
    return chat_completion.choices[0].message.content

# if __name__ == '__main__':
#     app.run(debug=True)
