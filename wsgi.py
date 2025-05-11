from main import app

if __name__ == "__main__":
    # Use waitress for production
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000, url_scheme='http', threads=6)
