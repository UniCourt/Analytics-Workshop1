# Use official Python runtime (Alpine Linux for minimal size)
FROM python:3.12-alpine

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install runtime dependencies only (postgresql-client for debugging)
RUN apk add --no-cache postgresql-client libpq

# Copy requirements file for better layer caching
COPY requirements.txt /app/

# Install Python dependencies
# Note: psycopg2-binary 2.9.9 has pre-built wheels for Python 3.12-alpine
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . /app

# Expose port for Flask app
EXPOSE 5000

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
