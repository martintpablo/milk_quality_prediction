FROM python:3.8
RUN pip install streamlit pandas scikit-learn
COPY src/* /app/
COPY model/milk_q_model.pkl /app/model/milk_q_model.pkl
WORKDIR /app
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
