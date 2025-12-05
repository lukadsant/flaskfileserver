import os
from flask import Flask, send_from_directory, abort

app = Flask(__name__)

# Directory where text files are stored
FILES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files')


@app.route('/file/<path:filename>')
def serve_file(filename):
    """Serve a text file from the files directory."""
    # Only allow .txt files
    if not filename.endswith('.txt'):
        abort(404)
    
    # Resolve the absolute path and check for path traversal
    file_path = os.path.normpath(os.path.join(FILES_DIR, filename))
    if not file_path.startswith(os.path.normpath(FILES_DIR) + os.sep):
        abort(404)
    
    # Check if the file exists
    if not os.path.isfile(file_path):
        abort(404)
    
    return send_from_directory(FILES_DIR, filename, mimetype='text/plain')


if __name__ == '__main__':
    # Ensure the files directory exists
    os.makedirs(FILES_DIR, exist_ok=True)
    debug_mode = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(debug=debug_mode)
