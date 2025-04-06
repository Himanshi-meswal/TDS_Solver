FROM python:3.11-slim

WORKDIR /app

# Copy only requirements first for caching
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Expose port 8008
EXPOSE 8008

# Start the app using uvicorn on port 8008
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8008"]