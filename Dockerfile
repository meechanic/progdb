FROM python:3-buster

ENV MAINDIRECTORY="/opt/app" \
  SROOT="/opt/static" \
  VENVPATH="/opt/venv" \
  DBPATH="/opt/db" \
  APPUSER=appuser

RUN mkdir -p "$SROOT" "$DBPATH" \
  && groupadd -r "$APPUSER" && useradd --no-log-init -r -g "$APPUSER" "$APPUSER" \
  && apt-get update \
  && apt-get install -y --no-install-recommends python3-venv postgresql-client-11 libpq-dev python3-dev

COPY . "$MAINDIRECTORY"/

RUN pyvenv "$VENVPATH" \
  && chown -R "$APPUSER":"$APPUSER" "$MAINDIRECTORY" "$SROOT" "$VENVPATH" "$DBPATH" \
  && . "$VENVPATH"/bin/activate \
  && pip install --upgrade pip setuptools wheel \
  && pip install -r "$MAINDIRECTORY"/requirements.txt

EXPOSE 8000

USER "$APPUSER":"$APPUSER"
#USER root

CMD . "$VENVPATH"/bin/activate && "$MAINDIRECTORY"/runner.sh
