FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/src

WORKDIR /app

COPY src/ /app/src/
COPY data/ /app/data/

RUN useradd --create-home --shell /usr/sbin/nologin podencoti \
    && chown -R podencoti:podencoti /app

USER podencoti

CMD ["python", "-m", "podencoti.app"]
