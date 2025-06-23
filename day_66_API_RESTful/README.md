# Cafe API

A RESTful API built with Flask and SQLAlchemy for managing a collection of cafes. This project allows you to add, search, update, and delete cafes, as well as retrieve random or all cafes from the database.

## Features

- Retrieve a random cafe
- List all cafes
- Search for cafes by location
- Add a new cafe (POST)
- Update the coffee price of a cafe (PATCH)
- Delete (report closed) a cafe (DELETE)

## Technologies Used

- Python 3
- Flask
- Flask-SQLAlchemy (with SQLAlchemy 2.0 style)
- SQLite

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/cafe-api.git
   cd cafe-api
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

5. **Access the API:**
   - The API will be running at `http://127.0.0.1:5000/`

## API Endpoints

| Method | Endpoint                       | Description                          |
|--------|------------------------------- |--------------------------------------|
| GET    | `/random`                      | Get a random cafe                    |
| GET    | `/all`                         | Get all cafes                        |
| GET    | `/search?loc=<location>`       | Search for a cafe by location        |
| POST   | `/add`                         | Add a new cafe                       |
| PATCH  | `/update-price/<cafe_id>`      | Update the coffee price of a cafe    |
| DELETE | `/report-closed/<cafe_id>`     | Delete (report closed) a cafe        |

## Postman Documentation

For detailed request/response examples and testing, view the full Postman documentation here:  
[https://documenter.getpostman.com/view/46107988/2sB2xCg8kQ](https://documenter.getpostman.com/view/46107988/2sB2xCg8kQ)

## Example Usage

### Add a Cafe (POST)
Send a POST request to `/add` with form data:
- `name`
- `map_url`
- `img_url`
- `location`
- `seats`
- `has_toilet` (`true` or `false`)
- `has_wifi` (`true` or `false`)
- `has_sockets` (`true` or `false`)
- `can_take_calls` (`true` or `false`)
- `coffee_price`

### Update Coffee Price (PATCH)
Send a PATCH request to `/update-price/<cafe_id>` with form data:
- `coffee_price`

### Report Closed (DELETE)
Send a DELETE request to `/report-closed/<cafe_id>`

## License

This project is licensed under the MIT License.

---

**Happy coding!**