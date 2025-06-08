```markdown
# Code Review Assistant

**Code Review Assistant** is an application designed to simplify code reviews during the software development process. The project consists of a backend API built with Python and Flask, and a simple frontend created using HTML and CSS.

---

## About the Project

This application allows developers to easily submit their code and receive quick feedback. The backend provides RESTful API services, while the frontend offers a clean and user-friendly interface.

---

## Technologies Used

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS  
- **API:** RESTful API

---

## Features

- API endpoints for code submission and review  
- Simple and intuitive user interface  
- Fast and reliable feedback mechanism

---

## Installation & Running

### Backend

1. Install required packages:

    ```bash
    pip install -r requirements.txt
    ```

2. Start the Flask API server:

    ```bash
    export FLASK_APP=app.py
    export FLASK_ENV=development
    flask run
    ```

> **Note:** On Windows PowerShell, use `set` instead of `export`:

```powershell
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```

### Frontend

Open the `index.html` file in any web browser to use the frontend interface.

---

## API Usage

| Endpoint       | Method | Description            |
| -------------- | ------ | ---------------------- |
| `/api/review`  | POST   | Submit code for review |

Example JSON payload:

```json
{
  "code": "print('Hello, world!')",
  "language": "python"
}
```

---

## Contributing

Thank you for your contributions! Please fork the repository, commit your changes, and create a pull request.

---

## License

Licensed under the MIT License.
```
