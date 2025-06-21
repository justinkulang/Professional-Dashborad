import os
import json

# Load configuration from config.json to get server host and port
# This assumes config.json is in the same directory or accessible
# For simplicity, this config loader is minimal compared to app.py's

_DEFAULT_HOST = "0.0.0.0"
_DEFAULT_PORT = 5000
_CONFIG_FILE = 'config.json'

try:
    with open(_CONFIG_FILE, 'r') as f:
        app_cfg = json.load(f)
    server_cfg = app_cfg.get('server', {})
    host = server_cfg.get('host', _DEFAULT_HOST)
    port = server_cfg.get('port', _DEFAULT_PORT)
except FileNotFoundError:
    print(f"WARNING: '{_CONFIG_FILE}' not found. Using default Gunicorn bind address {_DEFAULT_HOST}:{_DEFAULT_PORT}.")
    host = _DEFAULT_HOST
    port = _DEFAULT_PORT
except Exception as e:
    print(f"WARNING: Error loading '{_CONFIG_FILE}': {e}. Using default Gunicorn bind address {_DEFAULT_HOST}:{_DEFAULT_PORT}.")
    host = _DEFAULT_HOST
    port = _DEFAULT_PORT

# Gunicorn settings
bind = f"{host}:{port}"
workers = (os.cpu_count() * 2) + 1  # Standard Gunicorn recommendation

# Optional: Logging configuration for Gunicorn
# accesslog = '-'  # Log to stdout
# errorlog = '-'   # Log to stdout
# loglevel = 'info'

print(f"Gunicorn will bind to: {bind}")
print(f"Gunicorn will use {workers} workers.")
