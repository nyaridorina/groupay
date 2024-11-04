import os
from backend import create_app

# Create the Flask app instance using the factory function
app = create_app()

if __name__ == "__main__":
    # Get the port from the environment variable or default to 5000 for local development
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
