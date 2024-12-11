# Todo App

A Flask-based Todo application with user authentication, task management, and MongoDB integration.

## Features

- User registration and authentication
- Task creation and management
- Priority-based task organization
- MongoDB data persistence
- Comprehensive test coverage

## Prerequisites

- Python 3.x
- MongoDB
- pip (Python package manager)

## Installation

1. Clone the repository
```bash
git clone https://github.com/brissporras26/app_to_do_list.git
cd app_to_do_list
```

2. Create and activate virtual environment (recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure MongoDB
- Ensure MongoDB is installed and running
- Default connection string: `mongodb://localhost:27017/todo_app`

## Configuration

Create a `.env` file in the root directory:
```env
FLASK_APP=app
FLASK_ENV=development
MONGO_URI=mongodb://localhost:27017/todo_app
SECRET_KEY=your-secret-key
```

## Usage

1. Run the application:
```bash
python run.py
```

2. Access the application at: `http://localhost:5000`

## Testing

Run the test suite:
```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=app

# Run specific test file
pytest tests/test_system.py
```

## Documentation

Full documentation is available using MkDocs. To view:

1. Install documentation dependencies:
```bash
pip install -r requirements-docs.txt
```

2. Serve the documentation:
```bash
mkdocs serve
```

3. Access at: `http://127.0.0.1:8000`

## Project Structure

```
app_to_do_list/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── logic/
│       ├── users_logic.py
│       └── task_logic.py
├── tests/
│   ├── conftest.py
│   ├── test_system.py
│   └── test_user_logic.py
├── docs/
├── requirements.txt
├── requirements-docs.txt
└── run.py
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[MIT License](LICENSE)

## Contact

Your Name - your.email@example.com
Project Link: https://github.com/yourusername/app_to_do_list