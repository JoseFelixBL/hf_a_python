FROM alpine
RUN addgroup hfpython && adduser -S -G hfpython hfpython
USER hfpython
WORKDIR /usr/src/app
RUN mkdir var

# RUN mkdir /myvol
# # RUN echo "Hola mundo" > /myvol/saludos
# VOLUME /myvol