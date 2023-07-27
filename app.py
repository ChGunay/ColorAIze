import openai
from dotenv import dotenv_values
from flask import Flask, render_template, request
from collor_palette_generator import get_and_render_colors


config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]


app = Flask(__name__, template_folder='templates', static_folder='static',
            static_url_path='')


@app.route('/palette', methods=['POST'])
def prompt_to_palette():
    query = request.form['prompt']
    colors = get_and_render_colors(query)
    return {"colors": colors}

    # RETURN PALETTE


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
