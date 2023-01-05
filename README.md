# ChatGPT-GUI-vocal-assistant
This program is a GUI application that allows the user to input text by speaking into their microphone. The program animates a circle on the GUI while it is listening, and then inputs the recognized speech into a text box.

Once the user is finished speaking, the program sends the input text to the chat GPT API, which generates a response based on the input. The program then generates speech from the response text and plays it through the speaker.

The cli file contains functions for sending requests to the chat GPT API and generating speech from the response text, while the tkinter file contains the code for the GUI and the logic for handling the input and output of the chat GPT API.
