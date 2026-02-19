# Smart Bookmark Manager

A full-stack Django CRUD application to manage bookmarks.

## Features
- Add Bookmark (Title & URL)
- View All Bookmarks
- Update Bookmark
- Delete Bookmark

## Tech Stack
- Python
- Django
- SQLite
- Gunicorn
- Render (Deployment)

## Setup Instructions

1. Clone the repository:
   git clone https://github.com/seshadrimedabalimi2003-sudo/smart-bookmark-manager.git

2. Navigate to project folder:
   cd smart-bookmark-manager

3. Create virtual environment:
   python -m venv venv

4. Activate virtual environment:
   Windows:
   venv\Scripts\activate

5. Install dependencies:
   pip install -r requirements.txt

6. Run migrations:
   python manage.py migrate

7. Start the server:
   python manage.py runserver

Visit:
http://127.0.0.1:8000/

## Live Deployment
(Add your Render live URL here after deployment)