FROM python:3.12-slim
LABEL authors="dgogo"

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    wget \
    gnupg \
    ca-certificates \
    libgtk-3-0 \
    libdbus-glib-1-2 \
    libxt6 \
    libxrender1 \
    libxcomposite1 \
    libasound2 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    libfreetype6 \
    libx11-xcb1 \
    libxshmfence1 \
    libxv1 \
    libxcursor1 \
    libxss1 \
    xdg-utils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Firefox
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    firefox-esr \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


COPY main.py .
COPY requirements.txt .
COPY .env .
RUN pip install -r ./requirements.txt

CMD ["python3","./main.py"]
