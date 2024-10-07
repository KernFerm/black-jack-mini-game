# Use Python base image
FROM python:3.12.7-alpine

# Set working directory
WORKDIR /app

# Copy the project files from the current directory on host to /app in the container
COPY . /app

# Install dependencies if applicable
RUN pip install --no-cache-dir -r requirements.txt || true

# Run the application
CMD ["python", "blackjack.py"]
