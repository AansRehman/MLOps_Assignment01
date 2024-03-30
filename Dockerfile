# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies
RUN pip install --no-cache-dir flask pandas scikit-learn

# Expose the port Flask is running on
EXPOSE 5000

# Define the command to run your Flask app
CMD ["python", "main.py"]
