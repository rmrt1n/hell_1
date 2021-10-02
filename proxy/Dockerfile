FROM ubuntu:20.04
RUN apt update && apt install -y pip python ffmpeg libsm6 libxext6
WORKDIR /app
RUN mkdir /app/uploads
COPY requirements.txt app.py .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
