# learnify
## AI Teaching Tools

## Overview

**AI Teaching Tools** is a web application designed to assist educators in creating evaluations and exams using advanced artificial intelligence. This platform supports various educational tasks, including:

- **Evaluation Creation**: Generate and manage custom evaluations and exams.
- **Educational Planning**: Organize short-term, medium-term, and long-term teaching activities.
- **Student Tracking**: Monitor and track student progress and learning outcomes.
- **Report Generation**: Automatically produce detailed reports based on evaluations and student performance.

This tool aims to simplify and enhance the teaching process by leveraging AI to automate and improve various educational tasks.

## Installation

To get started with **AI Teaching Tools** on your local machine, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/ai-teaching-tools.git
   cd ai-teaching-tools
2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
3. **Activate the Virtual Environment**:
    - **Windows:**
       ```bash
       venv\Scripts\activate
    - **macOS/Linux**:
       ```bash
       source venv/bin/activate
4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
5. **Create a `.env` File**:
- In the project root directory, create a `.env` file with the following content:
   ```bash
   DATABASE_URI=sqlite:///site.db
   SECRET_KEY=your_secret_key_here
Replace `your_secret_key_here` with a secure key of your choice.   
6. **Run the Application**:
- Start the Flask development server by running:
   ```bash
   flask run
- Alternatively, you can use `run.py`:
   ```bash
   python run.py
The application will be accessible at `http://127.0.0.1:5000/` by default.
## Usage
1. **Authentication**: Sign up or log in to access the platform's features.
2. **Create Evaluations**: Use the evaluation tools to design and manage assessments.
3. **Plan Lessons**: Utilize planning tools for organizing educational activities.
4. **Track Students**: Monitor and assess student progress and outcomes.
5. **Generate Reports**: Create detailed reports based on evaluations and student performance.
## License
- This project is licensed under the MIT License. See the LICENSE file for details.
## Contact
- For any questions or feedback, please reach out to mohamedelwardi@yahoo.com.


   
