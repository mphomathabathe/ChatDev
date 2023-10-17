'''
This file contains the ChatBot class that handles the ML classification and provides answers to user questions.
'''
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
class ChatBot:
    def __init__(self):
        self.categories = ["category1", "category2", "category3"]  # Replace with actual categories
        self.questions = ["question1", "question2", "question3"]  # Replace with actual questions
        self.answers = ["answer1", "answer2", "answer3"]  # Replace with actual answers
        self.vectorizer = TfidfVectorizer()
        self.classifier = LogisticRegression()
        self.pipeline = Pipeline([
            ('vectorizer', self.vectorizer),
            ('classifier', self.classifier)
        ])
        self.train_model()
    def train_model(self):
        self.questions = self.vectorizer.fit_transform(self.questions)
        self.pipeline.fit(self.questions, self.categories)
    def get_answer(self, question):
        try:
            question = self.vectorizer.transform([question])
            category = self.pipeline.predict(question)[0]
            index = self.categories.index(category)
            return self.answers[index]
        except ValueError:
            return "I'm sorry, but I don't have an answer for that question."