# Day 59: Flask Blog Project

This project is a simple blog website built with Flask and styled using the StartBootstrap Clean Blog theme. It demonstrates how to use Flask routes, templates, and external APIs to create a dynamic blog.

## Features
- Home page listing all blog posts
- Individual post pages
- About and Contact pages
- Responsive design using Bootstrap
- Blog post data fetched from an external API (npoint.io)

## Project Structure
```
day_59_blog/
└── startbootstrap-clean-blog-gh-pages/
    ├── server.py                # Main Flask application
    ├── static/                  # Static assets (CSS, JS, images)
    └── templates/               # HTML templates
        ├── about.html
        ├── contact.html
        ├── footer.html
        ├── header.html
        ├── index.html
        ├── navbar.html
        └── post.html
```

## How It Works
- The Flask app fetches blog post data from a public API endpoint using the `requests` library.
- The home page (`/`) displays a list of blog posts with titles and subtitles.
- Clicking a post title navigates to the individual post page (`/post/<id>`).
- The About and Contact pages are static informational pages.

## Getting Started
1. **Install dependencies:**
   Ensure you have Python 3 and Flask installed. You may also need `requests`.
   ```powershell
   pip install flask requests
   ```
2. **Run the server:**
   ```powershell
   cd day_59_blog/startbootstrap-clean-blog-gh-pages
   python server.py
   ```
3. **Open your browser:**
   Visit `http://127.0.0.1:5000/` to view the blog.

## Customization
- To change the blog posts, update the data at the npoint.io API or modify the `get_posts()` function to use local data.
- You can edit the HTML templates in the `templates/` folder to change the look and feel.

## Credits
- [StartBootstrap Clean Blog](https://startbootstrap.com/theme/clean-blog) for the theme
- Flask and Jinja2 for the backend and templating

---
Enjoy your Flask-powered blog!
