import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    
    # api connection
    api_key = os.environ.get("GEMINI_API_KEY")
    # checking if api has value   
    if api_key == None:
        raise RuntimeError("couldn't find api key on environment")
    
    client = genai.Client(api_key=api_key)

    # parsing of the users prompts
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    # list of messages
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    
    # the actual generation of content?
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=messages
    )
    
    if response.usage_metadata == None:
        raise RuntimeError("API request was unsucessfull")
    if args.verbose == True:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(response.text)
    else:
        print(response.text)


   


if __name__ == "__main__":
    main()
