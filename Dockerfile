FROM python:3.9
COPY . /invoiceapp
WORKDIR /invoiceapp
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]