FROM python:3.9-slim

WORKDIR /app

COPY dashboard.py .

RUN pip install streamlit sqlalchemy pandas psycopg2-binary python-dotenv plotly

CMD ["streamlit", "run", "dashboard.py"]
