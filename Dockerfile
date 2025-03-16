FROM python:3.13.2-alpine3.21

RUN addgroup hfpython && adduser -S -G hfpython hfpython
USER hfpython

WORKDIR /usr/src/app

COPY --chown=hfpython requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=hfpython *.py .

EXPOSE 5000
CMD [ "python", "vsearchweb.py" ]
