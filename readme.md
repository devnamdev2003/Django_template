


# Django Template

## Overview

Django Template is a simple business web page based on Django. It includes an image slider to showcase various images related to the business and a contact form for users to get in touch.

## [Preview](https://djangopage.onrender.com/)

## Features

- Image Slider: A visually appealing image slider to showcase business-related images.
- Contact Form: A contact form that allows users to send inquiries or feedback.
- Responsiveness: The web page is designed to be responsive, adapting to different screen sizes and devices.

## Prerequisites

Before you begin, ensure you have the following prerequisites installed on your system:

- Python: The project requires Python to be installed. You can download the latest version of Python from the official website [Download](https://www.python.org/downloads/).

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/devnamdev2003/django-template.git
cd django-template
```

2. Create a virtual environment and activate it (recommended):

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Run database migrations:

```bash
python manage.py migrate
```

5. Create a superuser (optional but useful for testing the contact form):

```bash
python manage.py createsuperuser
```

6. Run the Django development server:

```bash
python manage.py runserver
```

7. Access the web page in your browser by navigating to `http://localhost:8000/`.


## License

This project is licensed under the [MIT License](LICENSE).

