def get_answer(self, question):
    try:
        question = self.vectorizer.transform([question])
        category = self.pipeline.predict(question)[0]
        index = self.categories.index(category)
        return self.answers[index]
    except ValueError:
        return "I'm sorry, but I don't have an answer for that question."