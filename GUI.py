import tkinter as tk
import threading
import cli
import speech_recognition as sr

class App:
    def __init__(self, master):
        # Set up the GUI
        self.frame = tk.Frame(master)
        self.frame.pack()
        self.canvas = tk.Canvas(self.frame, width=200, height=100)
        self.canvas.pack()
        self.text = tk.Text(self.frame, height=1)
        self.text.pack()
        self.button = tk.Button(self.frame, text="Start Listening", command=self.start_listening)
        self.button.pack()
        
        # Set up the animation
        self.circle = self.canvas.create_oval(50, 50, 150, 150, fill="red")
        self.animating = False
        
    def start_listening(self):
        # Start the animation
        self.animating = True
        self.animate()
        
        # Start the listening thread
        self.listening_thread = threading.Thread(target=self.listen)
        self.listening_thread.start()
        
    def listen(self):
        # Recognize speech and input it into the text box
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
        
        try:
            input_text = r.recognize_google(audio)
            print(f"You said: {input_text}")
            self.text.insert("end", input_text)
            
            # Send the input text to the chat GPT API and generate a response
            response_text = cli.send_request(input_text)
            cli.generate_response(response_text)
        except Exception as e:
            print("Sorry, I couldn't understand you.")
        
    def animate(self):
        # Animate the circle while the program is listening
        if self.animating:
            self.canvas.itemconfig(self.circle, fill="blue")
            self.frame.after(100, self.animate)
        else:
            self.canvas.itemconfig(self.circle, fill="red")

root = tk.Tk()
app = App(root)
root.mainloop()
