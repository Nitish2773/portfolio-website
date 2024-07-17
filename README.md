# Personal Portfolio Website

## Project Overview

This project is a personal portfolio website that showcases the developer's skills, projects, resume, and contact information. It is built using Django and styled with Bootstrap.

## Project Structure


## Libraries Used

- Django
- Bootstrap

## Description
This is a personal portfolio website built using Django. The website includes the following sections:
- **Home**: Dashboard layout with user profile picture and title "Full Stack Developer".
- **About**: Description, social media profiles, education, etc.
- **Skills**: Showcases frontend, backend, and database skills with icons.
- **Projects**: Categorizes projects under React, Django, HTML, CSS, JavaScript, Node.js, and Bootstrap.
- **Resume**: Complete resume and downloadable CSV.
- **Contact**: Contact information and feedback form.

## Features
- CRUD operations for managing content.
- Image uploads for profile picture and project images.
- Responsive design using Bootstrap.
- Dynamic content management via Django admin panel.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/portfolio-website.git
    cd portfolio-website
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

7. Access the website:
    Open your browser and go to `http://127.0.0.1:8000`

## Usage
- Navigate to the Django admin panel at `http://127.0.0.1:8000/admin` to manage your portfolio content.


https://github.com/user-attachments/assets/c7ef5833-99ef-4a09-b0b6-1514bb837380

