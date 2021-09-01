FROM ubuntu

ENV PYTHONUNBUFFERED=1

RUN apt update && \
    apt upgrade -y && \
    apt install python3 python3-pip curl -y

ADD https://raw.githubusercontent.com/RCD2020/lambda/main/Unit%203/docker_executables/upper.py .

ENTRYPOINT ["python3", "upper.py"]