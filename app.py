from flask import(
    Flask,
    request,
    render_template,
    redirect,
    send_from_directory,
    jsonify
)
import os
from werkzeug.utils import secure_filename
import shutil
import jsonify
from dotenv import load_dotenv
import sys

from langchain.chains.question_answering import load_qa_chain
from langchain.llms import PromptLayerOpenAI
from langchain.llms import OpenAI

from db_manager import init_chromadb, query_chromadb
from utils import create_prompt_template, initialize_memory

# load the environment variables from the .env file
load_dotenv()


# load base template
with open("./templates/base.txt", "r") as f:
    template = f.read()


# instantiate the router object
app = Flask(__name__)

# routes
@app.route('/api/answer', methods=['POST'])
async def answer():
    data = request.get_json()
    question = data["question"]
    docs = query_chromadb(db_dir="./data/chromadb/", query=question, k=3)

    prompt = create_prompt_template(template)

    memory = initialize_memory()

    await memory.init()

    chain = load_qa_chain(PromptLayerOpenAI(
        temperature=0,
        pl_tags=["user007", "publishingqa"]
        ), chain_type="stuff", memory=memory, prompt=prompt)

    response = chain({"input_documents": docs, "human_input": question}, return_only_outputs=True)
    return response


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == "POST":
        file = request.files.get('file')
        filename = file.filename

        if file:
            file_path = "./data/source_docs/" + secure_filename(file.filename)
            with open(file_path, 'wb') as f:
                shutil.copyfileobj(file, f)

        init_chromadb(db_dir="./data/chromadb/", file_path=file_path)

        return {"message": "200 - File uploaded successfully"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)