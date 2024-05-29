# Use an official Python runtime as a parent image
FROM python:3.10.2

# Set the working directory in the container
WORKDIR /frontend

# Copy the current directory contents into the container at /app
COPY . /frontend

RUN python3 -m venv venv 
RUN . venv/bin/activate

# Install any needed packages specified in requirements.txt
RUN venv/bin/pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80 443

# Define environment variable
ENV NAME World

# Run bot.py when the container launches
CMD ["vevn/bin/python3", "main.py"]
