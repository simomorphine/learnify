# learnify
## AI Teaching Tools

## Overview

**AI Teaching Tools** is a web application designed to assist educators in creating evaluations and exams using advanced artificial intelligence. This platform supports various educational tasks, including:

- **Evaluation Creation**: Generate and manage custom evaluations and exams.
- **Educational Planning**: Organize short-term, medium-term, and long-term teaching activities.
- **Student Tracking**: Monitor and track student progress and learning outcomes.
- **Report Generation**: Automatically produce detailed reports based on evaluations and student performance.

This tool aims to simplify and enhance the teaching process by leveraging AI to automate and improve various educational tasks.
## Technologies Involved

### Flask
- **Description**: A lightweight WSGI web application framework in Python. It is designed to be simple and easy to use, making it ideal for building web applications and APIs.
- **Key Features**: Routing, templating, and request handling.
- **Usage**: To create the web server, handle HTTP requests, and render templates.

### OpenAI Assistant API
- **Description**: An API provided by OpenAI that allows developers to integrate advanced language models into their applications. The API enables conversational interactions, content generation, and other language-based functionalities.
- **Key Features**: Natural language understanding, text generation, and context-aware responses.
- **Usage**: To generate intelligent responses and handle natural language queries from users.

### SQLAlchemy
- **Description**: A SQL toolkit and Object-Relational Mapping (ORM) library for Python. It provides a set of high-level API abstractions for database operations.
- **Key Features**: ORM, query construction, and database connection management.
- **Usage**: To interact with the database, manage data models, and perform CRUD operations.

### Jinja2
- **Description**: A templating engine for Python that integrates seamlessly with Flask. It allows for dynamic HTML generation and rendering.
- **Key Features**: Template inheritance, control structures, and template rendering.
- **Usage**: To render HTML templates and generate dynamic content for web pages.

### Bootstrap
- **Description**: A popular front-end framework for designing responsive and visually appealing web pages.
- **Key Features**: Pre-designed components, grid system, and responsive design utilities.
- **Usage**: To style the web application's user interface and ensure it is mobile-friendly.

### JavaScript
- **Description**: A programming language used for creating interactive elements on web pages.
- **Key Features**: Event handling, DOM manipulation, and asynchronous operations.
- **Usage**: To enhance user interactions and add dynamic features to the web application.

### SQLite
- **Description**: A lightweight, disk-based database engine that is self-contained and serverless.
- **Key Features**: Simple setup, zero-configuration, and compact size.
- **Usage**: To store and manage application data locally.
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


   
