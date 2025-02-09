FROM python:3.9-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install gunicorn and uvicorn explicitly
RUN pip install gunicorn uvicorn

# Copy the rest of the application code
COPY . .

# Specify the command to run your app with gunicorn and uvicorn worker
CMD ["gunicorn", "main:app", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]