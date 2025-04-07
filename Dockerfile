# Use the official Python 3.11 slim image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code into the container
COPY . .

# Expose port 8008
EXPOSE 8008

# Start the app using uvicorn on port 8008
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8008"]