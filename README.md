# Video Upload Application

## Overview

This is a Django-based web application for uploading and managing videos. The app allows users to upload videos, which are then stored on the server, and provides functionalities for viewing and commenting on uploaded videos.

## Features

- User authentication and authorization
- Video upload functionality
- Commenting system for each video
- Like functionality for videos
- Responsive design using Tailwind CSS

## Technologies Used

- **Backend:** Django, Django REST Framework
- **Frontend:** Angular
- **Database:** PostgreSQL (or your preferred database)
- **Storage:** Local storage (or AWS S3 if needed)
- **Styling:** Tailwind CSS

## Installation

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Django
- Node.js and npm
- Angular CLI

### Backend Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/CasualEngineerZombie/movie-dj.git
   cd movie-dj
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:

   - Create a PostgreSQL database (or use another database).
   - Update the `DATABASES` setting in `settings.py` with your database configuration.

5. Run migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

7. Start the Django development server:

   ```bash
   python manage.py runserver
   ```
 

## Usage

- Access the Django admin panel at [http://localhost:8000/admin](http://localhost:8000/admin). 
- Use the video upload form to add new videos and manage comments.