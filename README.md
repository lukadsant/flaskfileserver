# flaskfileserver

A simple Flask application to serve text files.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

1. Place your `.txt` files in the `files/` directory
2. Start the server:

```bash
python app.py
```

3. Access your files at `http://localhost:5000/file/<filename>`

Example: `http://localhost:5000/file/text1.txt`

## Configuration

- Set `FLASK_DEBUG=true` environment variable to enable debug mode