# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script and modelfile into the container
COPY app.py .
COPY modelfile .

# Install Ollama and set up the custom model
RUN pip install ollama
RUN ollama create Bony -f /app/modelfile

# Expose the port Gradio will run on
EXPOSE 7860

# Command to run the app
CMD ["python", "app.py"]