# My Library - Django Web Application

A full-featured Django web app for searching books via the Google Books API, saving favorites to a personal library, and managing your collection. This project demonstrates key web development concepts: external API integration, CRUD operations, and dynamic user interfaces.

---

## 🚀 Features

- **Search Books:** Find any book available on Google Books.
- **View Results:** See covers, authors, and publication dates.
- **Save Favorites:** Add books to your personal library.
- **Manage Collection:** Edit or delete saved books.
- **Django MVT Architecture:** Structured for clarity and scalability.

---

## 🛠️ Built With

- Python
- Django
- Bootstrap 5
- Google Books API
- Requests

---

## 📚 Key Concepts

- **Django Project & App Structure**
    - New project/app setup (`books`)
    - `settings.py` configuration
    - MVT (Model-View-Template) architecture

- **Database Modeling & Migrations**
    - `Book` model with various field types
    - `makemigrations` and `migrate`
    - Unique `google_id` for deduplication

- **External API Integration**
    - GET requests to Google Books API
    - JSON parsing and safe data extraction
    - Dynamic query URLs

- **Full CRUD Functionality**
    - **Create:** Save books from API
    - **Read:** Display books from API and database
    - **Update:** Edit saved book details
    - **Delete:** Remove books from collection

- **Django Views & URL Routing**
    - Function-based views for user actions
    - URL mapping in `urls.py`
    - Named URLs for maintainable templates
    - Handling GET and POST requests

- **Dynamic Template Rendering**
    - Django template language (`{% for %}`, `{% if %}`, `{% empty %}`)
    - Passing context data
    - Reusable components (`{% include %}`)

- **HTML Forms & CSRF Protection**
    - Forms for search and data submission
    - Hidden fields for passing data
    - CSRF protection (`{% csrf_token %}`)

---

## 🏁 Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

1. **Clone the repo:**
     ```bash
     git clone <repo-url>
     cd <repo-directory>
     ```

2. **Create a virtual environment (recommended):**
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```

3. **Install dependencies:**
     ```bash
     pip install -r requirements.txt
     ```

4. **Apply database migrations:**
     ```bash
     python manage.py migrate
     ```

5. **Run the development server:**
     ```bash
     python manage.py runserver
     ```

6. **Open your browser:**
     - Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

Enjoy managing your personal book library!