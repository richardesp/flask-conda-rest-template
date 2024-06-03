FROM continuumio/miniconda3

WORKDIR /app

# Copy config files and environment for dev dependencies
COPY /environments/prod.yml /app/

# Create and activate conda environment
RUN conda env create -f prod.yml
RUN echo "source activate myenv" > ~/.bashrc
ENV PATH /opt/conda/envs/myenv/bin:$PATH

# Copy Flask backend code to the container
COPY backend /app/backend
WORKDIR /app

# Execute this script to get all certificates from digital ocean
COPY get_secrets.py /app/get_secrets.py
RUN python /app/get_secrets.py

# Expose proxy pass nginx port
EXPOSE 5000

# Command to execute gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "backend.main:app"]
