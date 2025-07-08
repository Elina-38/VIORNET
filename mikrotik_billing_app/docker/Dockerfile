# Use Alpine Linux as a base image for a smaller footprint
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY ./src /app/src

# Expose the port the app runs on
EXPOSE 8080

# Command to run the application
CMD ["python", "src/main.py"]
