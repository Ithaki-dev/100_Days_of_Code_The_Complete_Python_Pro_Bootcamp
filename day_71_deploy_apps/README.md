# 📝 Flask Blog with User Authentication

A modern, secure blog application built with Flask that features user authentication, rich text editing, and a responsive design. Users can register, log in, create, edit, and delete blog posts with a clean, professional interface.

![Flask](https://img.shields.io/badge/Flask-3.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-orange)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple)

## 🌟 Features

### 🔐 User Authentication
- **User Registration**: Secure account creation with email validation
- **User Login/Logout**: Session management with Flask-Login
- **Password Security**: Passwords hashed using Werkzeug's PBKDF2-SHA256
- **Protected Routes**: Only authenticated users can create/edit/delete posts

### 📖 Blog Management
- **Create Posts**: Rich text editor (CKEditor) for writing blog posts
- **Edit Posts**: Modify existing blog posts with pre-populated forms
- **Delete Posts**: Remove unwanted blog posts
- **View Posts**: Clean, readable post display with responsive design
- **Post Metadata**: Automatic date stamping and author attribution

### 🎨 User Interface
- **Responsive Design**: Bootstrap 5 for mobile-friendly layouts
- **Rich Text Editing**: CKEditor integration for WYSIWYG editing
- **Flash Messages**: User feedback for actions (success/error messages)
- **Clean Navigation**: Intuitive header and footer components
- **Modern Styling**: Professional appearance with custom CSS

### 🛡️ Security Features
- **CSRF Protection**: Flask-WTF forms with CSRF tokens
- **SQL Injection Protection**: SQLAlchemy ORM prevents SQL injection
- **Session Security**: Secure session management
- **Input Validation**: Form validation for all user inputs

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/flask-blog-auth.git
   cd flask-blog-auth
   ```

2. **Create and activate virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python main.py
   ```

5. **Access the application:**
   Open your browser and navigate to `http://localhost:5002`

## 📁 Project Structure

```
day_69_blog_users/
├── main.py                 # Main Flask application
├── forms.py               # WTForms form definitions
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── instance/
│   └── posts.db          # SQLite database (auto-created)
├── static/
│   ├── assets/           # Images and media files
│   ├── css/              # Custom stylesheets
│   └── js/               # JavaScript files
└── templates/
    ├── header.html       # Navigation header
    ├── footer.html       # Page footer
    ├── index.html        # Homepage (blog list)
    ├── post.html         # Individual post view
    ├── make-post.html    # Create/edit post form
    ├── register.html     # User registration form
    ├── login.html        # User login form
    ├── about.html        # About page
    └── contact.html      # Contact page
```

## 🛠️ Technologies Used

### Backend
- **Flask 3.0+**: Web framework
- **SQLAlchemy 2.0+**: Database ORM
- **Flask-Login**: User session management
- **Flask-WTF**: Form handling and CSRF protection
- **Werkzeug**: Password hashing utilities

### Frontend
- **Bootstrap 5**: CSS framework for responsive design
- **CKEditor**: Rich text editor for blog content
- **Jinja2**: Template engine (built into Flask)

### Database
- **SQLite**: Lightweight database for development
- **Database Models**:
  - `User`: Stores user accounts (id, username, email, password)
  - `BlogPost`: Stores blog posts (id, title, subtitle, body, author, date, img_url)

## 📋 API Endpoints

| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|----------------|
| GET | `/` | View all blog posts | No |
| GET/POST | `/register` | User registration | No |
| GET/POST | `/login` | User login | No |
| GET | `/logout` | User logout | Yes |
| GET | `/post/<id>` | View specific post | No |
| GET/POST | `/new-post` | Create new post | Yes |
| GET/POST | `/edit-post/<id>` | Edit existing post | Yes |
| GET | `/delete/<id>` | Delete post | Yes |
| GET | `/about` | About page | No |
| GET | `/contact` | Contact page | No |

## 🔧 Configuration

### Environment Variables
The application uses the following configuration:
- `SECRET_KEY`: Used for session security (currently hardcoded - change for production)
- `SQLALCHEMY_DATABASE_URI`: Database connection string

### Database Configuration
- **Development**: SQLite database stored in `instance/posts.db`
- **Production**: Can be configured to use PostgreSQL, MySQL, etc.

## 🚦 Usage Guide

### For Users
1. **Register**: Create an account with username, email, and password
2. **Login**: Access your account using email and password
3. **Create Posts**: Use the rich text editor to write blog posts
4. **Manage Content**: Edit or delete your posts as needed
5. **Browse**: Read posts from other users

### For Developers
1. **Add Features**: Extend functionality by modifying `main.py`
2. **Customize Templates**: Edit HTML templates in the `templates/` directory
3. **Style Changes**: Modify CSS in the `static/css/` directory
4. **Database Changes**: Update models and run migrations

## 🔒 Security Best Practices

- ✅ Passwords are hashed using PBKDF2-SHA256
- ✅ CSRF protection on all forms
- ✅ SQL injection prevention with SQLAlchemy ORM
- ✅ Session management with Flask-Login
- ✅ Input validation on all forms

### Production Security Recommendations
- Change the `SECRET_KEY` to a secure, random value
- Use environment variables for sensitive configuration
- Implement HTTPS in production
- Add rate limiting for login attempts
- Consider implementing email verification

## 🧪 Testing

To test the application:

1. **Register a new user**
2. **Login with the created account**
3. **Create a new blog post**
4. **Edit the blog post**
5. **Delete the blog post**
6. **Logout and verify protected routes are inaccessible**

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is part of the "100 Days of Code: The Complete Python Pro Bootcamp" course. Feel free to use this code for learning purposes.

## 🐛 Known Issues

- Author field in edit form shows the current user instead of original author
- No pagination for blog posts (will be slow with many posts)
- No user profile management features
- No comment system for blog posts

## 🚀 Future Enhancements

- [ ] Add user profile pages
- [ ] Implement comment system
- [ ] Add post categories and tags
- [ ] Implement search functionality
- [ ] Add post pagination
- [ ] Email verification for registration
- [ ] Password reset functionality
- [ ] Admin panel for user management
- [ ] Image upload for posts
- [ ] Social media sharing buttons

## 📞 Support

If you encounter any issues or have questions:
1. Check the existing issues in the repository
2. Create a new issue with a detailed description
3. Include steps to reproduce the problem

## 🎯 Learning Objectives

This project demonstrates:
- Flask web application development
- User authentication and session management
- Database design and ORM usage
- Form handling and validation
- Template inheritance and Jinja2
- Security best practices in web development
- RESTful routing patterns

---

**Happy Blogging!** 🎉

*This project is part of Day 69 of the 100 Days of Code: The Complete Python Pro Bootcamp.*
