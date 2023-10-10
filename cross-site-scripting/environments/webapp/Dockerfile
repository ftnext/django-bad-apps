FROM python:3.11-bookworm as builder
WORKDIR /code
COPY requirements.lock /code/
RUN pip install --no-cache-dir -r requirements.lock
RUN SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())') && \
cat <<ENV_FILE > .env
DEBUG=True
SECRET_KEY=${SECRET_KEY}
DATABASE_URL=postgres://developer:mysecretpassword@db/badapp
ENV_FILE

FROM python:3.11-bookworm
WORKDIR /code
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY bad_xss /code/
COPY --from=builder /code/.env /code/.env
COPY environments/webapp/entrypoint.sh /code/
CMD [ "./entrypoint.sh" ]
