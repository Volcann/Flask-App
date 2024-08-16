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

# Ensure the virtual environment is used for subsequent commands
ENV PATH="/app/venv/bin:$PATH"

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the required Python packages in the virtual environment
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir numpy \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Define the command to run your app using gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:${PORT:-5000}", "app:app"]
