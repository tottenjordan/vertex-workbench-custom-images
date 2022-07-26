FROM ubuntu:20.04

## for apt to be noninteractive
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

RUN apt-get update && apt-get install -y \
    python3.9 \
    python3-pip

# Use this to set the default python to 3.9
# RUN sudo update-alternatives  --set python /usr/bin/python3.9
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1
RUN update-alternatives --set python3 /usr/bin/python3.9

RUN pip install jupyter -U && pip install jupyterlab

# RUN python3.9 -m pip install ipykernel && python3.9 -m ipykernel install --user --name "python-3.9"

EXPOSE 8080
             
RUN mkdir /root/.jupyter
             
COPY scratch_container/jupyter_notebook_config.py /root/.jupyter

ENV pwd=""

ENTRYPOINT exec jupyter-lab --ip=0.0.0.0 --port=8080 --no-browser --allow-root --ServerApp.allow_origin="*" --NotebookApp.token="$pwd" --NotebookApp.password="$pwd"
