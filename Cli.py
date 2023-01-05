import requests
import json
import pyttsx3

# Set the API endpoint URL
api_url = "https://api.chatgpt.com/response"

# Set the API key
api_key = "YOUR_API_KEY"

# Set the headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

def send_request(input_text):
    # Send the input text to the chat GPT API
    data = {
        "input": input_text
    }
    response = requests.post(api_url, headers=headers, json=data)
    
    # Check the status code of the response
    if response.status_code == 200:
        # Return the response text if the request is successful
        return response.json()["response"]
    else:
        # Return an error message if the request is unsuccessful
        return "Sorry, there was an error with the request."

def generate_response(response_text):
    # Generate speech from the response text
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("voice", "com.apple.speech.synthesis.voice.siri")
    engine.say(response_text)
    engine.runAndWait()
