import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file

system_prompt = """- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files
"""



available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    try:
        if len(sys.argv) == 3:
            print(sys.argv) 
                     
            messages = [
                            types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
                    ]       
            
            response = client.models.generate_content(
                model='gemini-2.0-flash-001', 
                contents=messages ,
                config=types.GenerateContentConfig( tools=[available_functions],
                                                   system_instruction=system_prompt)) 
            print(f"User prompt: {sys.argv[1]}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
            print(response.text)
            print(f"Calling function: {response.function_calls[0].name}({response.function_calls[0].args})" )

            sys.exit(0)
        else:
            
            try:
                new_text=sys.argv[1]
                print(new_text) 
                
            except Exception as e:
                print(f"please input some prompt text. Error: {e}") 
                sys.exit(1)     
            messages = [
                            types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
                    ]       
            
            response = client.models.generate_content(
                model='gemini-2.0-flash-001', 
                contents=messages ,
                config=types.GenerateContentConfig( tools=[available_functions],
                                                   system_instruction=system_prompt)) 
            print(response.text)
            print(f"Calling function: {response.function_calls[0].name}({response.function_calls[0].args})" )
            
            sys.exit(0)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
