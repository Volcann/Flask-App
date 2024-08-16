# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libatlas-base-dev \
    gfortran \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Create a virtual environment
RUN python -m venv venv

# Activate the virtual environment and install the required packages
RUN venv/bin/pip install --no-cache-dir --upgrade pip \
    && venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Define the command to run your app using gunicorn
CMD ["venv/bin/gunicorn", "-b", "0.0.0.0:5000", "app:app"]
