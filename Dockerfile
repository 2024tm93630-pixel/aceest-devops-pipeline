# Use a lightweight Python image 
FROM python:3.9-slim

# Set the working directory inside the container 
WORKDIR /app

# Copy the requirements file and install dependencies [cite: 10, 16]
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container [cite: 10, 16]
# Note: This copies everything from your folder to the /app folder
COPY . .

# Expose the port Flask runs on [cite: 10, 24]
EXPOSE 5000

# Run the application 
# We use 'app.py' directly because it is now in the /app folder
CMD ["python", "app.py"]