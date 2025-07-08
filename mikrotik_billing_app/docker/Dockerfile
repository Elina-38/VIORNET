# Use Alpine Linux as a base image for a smaller footprint
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Install system dependencies that might be needed by Python packages (e.g., for cryptography if routeros-api needs it)
# RUN apk add --no-cache some-build-dependencies-if-needed

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
# Using --no-cache-dir to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the main application file that sets FLASK_APP for migrations
COPY app.py .
# Copy the migrations directory
COPY migrations ./migrations
# Copy the rest of the application source code
COPY ./src ./src

# Expose the port the app runs on
EXPOSE 8080

# Environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080
# DATABASE_DIR will default to /app/data as per src/main.py, can be overridden
# ENV DATABASE_DIR=/app/data

# Create the data directory if it's not created by a volume mount automatically
# This directory is intended to be a mount point for persistent storage.
RUN mkdir -p /app/data

# Command to run the application
# For production, gunicorn is recommended. For now, using Flask's dev server.
# CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
CMD ["python", "-m", "flask", "run"]

# Note on Database Migrations:
# Database migrations (flask db upgrade) should be run as part of the deployment process,
# typically after the image is built and before the new container starts, or as an entrypoint script.
# They are not run during the image build process itself to keep the image generic.
# Example: docker run ... <image_name> flask db upgrade && python -m flask run
# Or a more robust entrypoint script in the container.
