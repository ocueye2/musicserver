# Start with your base image
FROM  python:3.12.3-slim


WORKDIR /app

# clone repo
RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    git clone https://github.com/ocueye2/musicserver.git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


RUN pip install flask

# Make port 8080 available to the world outside this container
EXPOSE 4323

WORKDIR /app/my-website
# Run app.py when the container launches
CMD ["python", "server.py"]
