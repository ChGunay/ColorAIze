# AI Color Palette Generator

AI Color Palette Generator is a web application that uses OpenAI's GPT-3 model to generate a color palette based on a specific theme. You can use the application by writing a statement about any theme or emotion you want, and the AI will create a color palette for you.


## Getting Started

### Prerequisites

- Python 3.7 or higher
- Flask 1.1.2 or higher
- dotenv 0.19.0 or higher
- openai 0.27.0 or higher

### Installation

1. First, clone the project to your local machine:

```bash
git clone https://github.com/YourUsername/YourRepo.git
```

2. Go into the cloned folder:
```bash
cd ./ColorAIze
```


3. Create and activate a Python virtual environment:

```bash
python3 -m venv env
source env/bin/activate
```


4. Install the required Python packages:
```bash
pip install -r requirements.txt
```


5. Add your OpenAI API key to the `.env` file:
```bash
echo "OPENAI_API_KEY=your_api_key" > .env
```


6. Start the application:
```bash
python app.py
```


