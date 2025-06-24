# Flask Blog RESTful Application

A simple blog platform built with Flask, SQLAlchemy, Flask-WTF, and CKEditor. This project demonstrates RESTful routing, form handling, and database integration for creating, editing, and deleting blog posts.

## Features

- View all blog posts on the home page
- View individual blog posts
- Create new blog posts with a rich text editor (CKEditor)
- Edit existing blog posts
- Delete blog posts
- About and Contact static pages
- Responsive Bootstrap 5 styling

## Technologies Used

- Python 3
- Flask
- Flask-Bootstrap (Bootstrap 5)
- Flask-SQLAlchemy
- Flask-WTF
- Flask-CKEditor
- WTForms
- SQLite

## Project Structure

```
day_67_blog_RESTful/
│
├── main.py
├── instance/
│   └── posts.db
├── templates/
│   ├── index.html
│   ├── post.html
│   ├── make-post.html
│   ├── about.html
│   └── contact.html
├── static/
│   └── assets/
│       └── img/
└── requirements.txt
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/flask-blog-restful.git
   cd flask-blog-restful/day_67_blog_RESTful
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**
   ```bash
   python -m pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python main.py
   ```

5. **Open your browser and go to:**
   ```
   http://127.0.0.1:5003/
   ```

## Usage

- **Home Page:** Lists all blog posts.
- **Create New Post:** Click "Create New Post" to add a new blog entry.
- **Edit Post:** Click the edit button on a post to update it.
- **Delete Post:** Click the delete button (styled as a link) to remove a post.
- **About/Contact:** Access via the navigation bar.

## Notes

- The database file (`posts.db`) is created automatically in the `instance` folder.
- CKEditor is used for rich text editing in the blog post body.
- The app runs in debug mode on port 5003 by default.

## License

This project is licensed under the MIT License.

---

**Happy blogging!**