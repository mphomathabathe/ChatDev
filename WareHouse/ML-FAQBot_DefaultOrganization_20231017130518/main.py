'''
This is the main file that will be executed to run the FAQ chatbot.
'''
from tkinter import Tk, Frame, Label, Entry, Button, Text, Scrollbar
from chatbot import ChatBot
class ChatBotGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("FAQ Chatbot")
        self.frame = Frame(self.master)
        self.frame.pack(pady=10)
        self.label = Label(self.frame, text="Enter your question:")
        self.label.pack()
        self.entry = Entry(self.frame, width=50)
        self.entry.pack(pady=10)
        self.button = Button(self.frame, text="Ask", command=self.ask_question)
        self.button.pack()
        self.text = Text(self.master, width=60, height=10)
        self.text.pack(pady=10)
        self.scrollbar = Scrollbar(self.master)
        self.scrollbar.pack(side="right", fill="y")
        self.text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text.yview)
        self.chatbot = ChatBot()
    def ask_question(self):
        question = self.entry.get()
        answer = self.chatbot.get_answer(question)
        self.text.insert("end", f"Question: {question}\n")
        self.text.insert("end", f"Answer: {answer}\n\n")
        self.entry.delete(0, "end")
if __name__ == "__main__":
    root = Tk()
    chatbot_gui = ChatBotGUI(root)
    root.mainloop()