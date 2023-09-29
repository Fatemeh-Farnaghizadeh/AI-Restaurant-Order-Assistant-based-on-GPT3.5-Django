# AI Restaurant Order Assistant

Welcome to the AI Restaurant Order Assistant project! This project combines the power of GPT-3.5 Turbo and Django to revolutionize the dining experience by streamlining the food ordering process.

## Demo Video

Watch My demo video to see the AI Restaurant Order Assistant in action:

<video width="640" height="360" controls autoplay>
  <source src="https://github.com/Fatemeh-Farnaghizadeh/AI-Restaurant-Order-Assistant-based-on-GPT3.5-Django/blob/master/Demo.gif" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Key Features

- **Personalized Recommendations:** My AI-powered assistant uses GPT-3.5 Turbo to provide personalized menu recommendations based on user preferences.

- **Django Integration:** Seamlessly integrated with Django, ensuring a robust and user-friendly experience for both customers and restaurant staff.

- **Eliminate Wait Times:** Say goodbye to long waits and order errors. My system ensures quicker and more accurate food ordering.

## Getting Started

To get started with the AI Restaurant Order Assistant, follow these steps:

1. **Clone the Repository:** `git clone https://github.com/Fatemeh-Farnaghizadeh/AI-Restaurant-Order-Assistant-based-on-GPT3.5-Django.git`

2. **Create a Python Virtual Environment (venv), Activate It, and Install Required Packages:** 
   - Navigate to the project directory.
   - Create a virtual environment using the following command:

     ```bash
     python -m venv venv
     ```

   - Activate the virtual environment using the appropriate commands for your platform (e.g., `source venv/bin/activate` on Linux/macOS or `venv\Scripts\activate` on Windows).

   - Install the required packages listed in `requirements.txt` by running the following command:

     ```bash
     pip install -r requirements.txt
     ```

3. **Create an OpenAI API Key:** 
   - Create an OpenAI account and obtain an API key.

4. **Create a `secret_key.py` File:** 
   - In the project directory, navigate to the "assistant" folder.
   - Create a new file named `secret_key.py` if it doesn't already exist.
   - Inside `secret_key.py`, define a variable `API_KEY` and set it to your OpenAI API key, like this:

     ```python
     API_KEY = "open ai api key"
     ```

5. **Run the Development Server:** In the path of the `manage.py` file, run this command:

   ```bash
   python manage.py runserver
