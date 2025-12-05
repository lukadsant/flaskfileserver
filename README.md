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

## Deploy to Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/flaskfileserver)

### Manual Deployment

1. Install the [Railway CLI](https://docs.railway.app/develop/cli)
2. Login to Railway:
   ```bash
   railway login
   ```
3. Initialize a new project:
   ```bash
   railway init
   ```
4. Deploy your application:
   ```bash
   railway up
   ```

The application will automatically:
- Use the `PORT` environment variable provided by Railway
- Start with Gunicorn as the WSGI server