# AI AGENT (GOOGLE GEMINI ) 
## Prequisites
- Have python uv package manager install 
```bash 
## Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
## Windows 
wget -qO- https://astral.sh/uv/install.sh | sh
```
Or access installation details through [UV Website](https://docs.astral.sh/uv/getting-started/installation/)

- Create virtual Enviroment
```bash
uv venv
```
- Activate the enviroment 
```bash 
source .venv/bin/activate
```
- Add dependencies for the project 
```bash 
uv add google-genai==1.12.1
uv add python-dotenv==1.1.0
```
- Create an .env File with your Gemini APi
```bash
GEMINI_API_KEY="your_api_key_here"
```

- To run the agent 
```bash 
un run main.py "your prompt"
```

Feel free to add any modifications and forks :)  Have fun 
