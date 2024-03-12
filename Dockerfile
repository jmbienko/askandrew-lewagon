FROM python:3.10-slim-bookworm

WORKDIR /prod

# We strip the requirements from useless packages like `ipykernel`, `matplotlib` etc...
COPY requirements.txt requirements.txt
#RUN export HNSWLIB_NO_NATIVE=1
RUN pip install -r requirements.txt
#--no-cache-dir
#RUN apt-get -y update
#RUN apt-get install -y sqlite3 libsqlite3-dev


COPY askandrew askandrew
COPY setup.py setup.py
RUN pip install .

#COPY Makefile Makefile
#RUN make reset_local_files

CMD uvicorn askandrew.api.api:app --host 0.0.0.0 --port $PORT
# $DEL_END
