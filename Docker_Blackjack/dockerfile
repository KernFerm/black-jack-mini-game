# Use Python base image
FROM python:3.11-slim

# Install Tkinter and related packages
RUN apt-get update && apt-get install -y python3-tk libx11-6

# Set working directory
WORKDIR /app

# Copy the project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python", "blackjack.py"]
