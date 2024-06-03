FROM continuumio/miniconda3

WORKDIR /app

# Copy config files and environment for dev dependencies
COPY /environments/dev.yml /app/

# Create and activate conda environment
RUN conda env create -f dev.yml
RUN echo "source activate dev_env" > ~/.bashrc
ENV PATH /opt/conda/envs/dev_env/bin:$PATH

# Copy Flask backend code to the container
COPY backend /app/backend
WORKDIR /app

# Expose proxy pass nginx port
EXPOSE 5000

# Command to execute flask app using debug mode (development)
CMD ["flask", "run", "--host=0.0.0.0"]
