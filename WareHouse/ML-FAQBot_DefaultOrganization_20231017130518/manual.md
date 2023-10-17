# ChatDev FAQ Chatbot User Manual

## Introduction

The ChatDev FAQ Chatbot is a machine learning-based chatbot designed to provide answers to frequently asked questions. It uses ML classification techniques to categorize user questions and provide relevant answers. This user manual will guide you through the installation process, explain the main functions of the software, and provide instructions on how to use it effectively.

## Installation

To install the ChatDev FAQ Chatbot, follow these steps:

1. Make sure you have Python installed on your system. You can download Python from the official website: https://www.python.org/downloads/

2. Clone the ChatDev repository from GitHub using the following command:

   ```
   git clone https://github.com/ChatDev/FAQ-Chatbot.git
   ```

3. Navigate to the project directory:

   ```
   cd FAQ-Chatbot
   ```

4. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

5. Once the installation is complete, you are ready to use the ChatDev FAQ Chatbot.

## Main Functions

The ChatDev FAQ Chatbot provides the following main functions:

1. **Ask a Question**: Enter your question in the provided input field and click the "Ask" button. The chatbot will process your question and provide an answer based on the trained ML classification model.

2. **View Answer**: The chatbot will display the question you asked and the corresponding answer in the text area below the input field. You can scroll through the chat history to view previous questions and answers.

## Usage

To use the ChatDev FAQ Chatbot, follow these steps:

1. Open a terminal or command prompt and navigate to the project directory.

2. Run the following command to start the chatbot:

   ```
   python main.py
   ```

3. The chatbot GUI window will open. Enter your question in the input field and click the "Ask" button.

4. The chatbot will process your question and display the question and answer in the text area.

5. Repeat steps 3 and 4 to ask additional questions.

6. To exit the chatbot, close the GUI window.

## Customization

To customize the chatbot with your own FAQ data, follow these steps:

1. Open the `chatbot.py` file in a text editor.

2. Replace the placeholder categories, questions, and answers with your own data. Make sure to maintain the same structure and format.

3. Save the changes and run the chatbot using the instructions provided in the "Usage" section.

## Troubleshooting

If you encounter any issues while using the ChatDev FAQ Chatbot, try the following troubleshooting steps:

1. Make sure you have installed all the required dependencies listed in the `requirements.txt` file.

2. Check that your Python version is compatible with the dependencies. The recommended Python version is 3.7 or higher.

3. Verify that your internet connection is stable, as the chatbot may require internet access to download additional resources.

4. If you are still experiencing issues, please refer to the project's GitHub repository for known issues or open a new issue if necessary: https://github.com/ChatDev/FAQ-Chatbot/issues

## Conclusion

Congratulations! You have successfully installed and learned how to use the ChatDev FAQ Chatbot. This chatbot can be a valuable tool for providing quick and accurate answers to frequently asked questions. Feel free to customize it according to your specific needs and enjoy the benefits of ML classification in your FAQ chatbot.