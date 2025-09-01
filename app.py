import openai
from flask import Flask, render_template, jsonify, request
import langchain
from langchain_core.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain
from langchain_community.llms import OpenAI


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/generate', methods = ['GET', 'POST'])
def generate():
    if request.method == 'POST':
        prompt = PromptTemplate.from_template("Generate a blog on title {title}")
        llm = OpenAI(openai_api_key = 'api_key', temperature = 0.3)
        chain = LLMChain(llm = llm, prompt = prompt)
        prompt = request.json.get('prompt')
        output = chain.run(prompt)
        print(output)
        return output


if __name__ == '__main__':
    app.run()
