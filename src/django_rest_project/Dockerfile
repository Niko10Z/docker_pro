FROM python:3.11
SHELL ["/bin/bash", "-c"]
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN useradd -rms /bin/bash user_djan
WORKDIR /home/user_djan
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./django_rest_project ./django_project/django_rest_project
COPY ./docstore ./django_project/docstore
COPY ./manage.py ./django_project/
WORKDIR ./django_project
RUN mkdir ./static && mkdir ./media && chown -R user_djan:user_djan /home/user_djan && chmod 755 /home/user_djan
