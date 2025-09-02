import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    try:
        if len(sys.argv) == 3:
            print(sys.argv[2])          
            messages = [
                            types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
                    ]       
            
            response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages) 
            print(f"User prompt: {sys.argv[1]}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
            print(response.text)

            sys.exit(0)
        else:
            print(sys.argv[1])          
            messages = [
                            types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
                    ]       
            
            response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages) 
            print(response.text)
            
            sys.exit(0)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
