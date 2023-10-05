FROM python:3.11-bookworm as builder
WORKDIR /code
COPY requirements.lock /code/
RUN pip install --no-cache-dir -r requirements.lock

FROM python:3.11-bookworm
WORKDIR /code
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY bad_xss /code/
COPY environments/webapp/entrypoint.sh /code/
CMD [ "./entrypoint.sh" ]
