FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install --no-cache-dir pycryptodome
RUN pip install sympy
# Make port 7777 available to the world outside this container
EXPOSE 7778

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "server.py"]

# docker build -t time_line .
# docker run --name=time_line -p 7799:7777 time_line