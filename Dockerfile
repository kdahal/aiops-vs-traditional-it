# Use a specific, stable base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy dependency file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY src /app/src

# Command to run the AIOps correlator service
CMD ["uvicorn", "src.alert_correlator.correlator:app", "--host", "0.0.0.0", "--port", "8000"]
