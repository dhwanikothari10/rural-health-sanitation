from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key (you can also load this from an environment variable)
openai.api_key = "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"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def chatbot_response():
    user_input = request.form['msg']
    response = generate_gpt_response(user_input)
    return jsonify({'response': response})

def generate_gpt_response(user_input):
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful chatbot that educates people in rural areas about health, hygiene, clean water, and sanitation."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7
        )
        return completion.choices[0].message['content'].strip()
    except Exception as e:
        return "Sorry, I couldn't process that right now."

if __name__ == '__main__':
    app.run(debug=True)
