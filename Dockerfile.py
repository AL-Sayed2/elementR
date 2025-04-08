FROM python:3.12-slim-buster

# Install system dependencies required by OpenCV (including OpenGL)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    libxrender1 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Set up the working directory inside the container
WORKDIR /app

# Copy your application files into the container
COPY . /app

# Install your Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define the command to run your application
CMD ["python", "app.py"]
