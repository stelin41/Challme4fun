FROM alpine:3.19

RUN apk update
RUN apk add --no-cache gcc musl-dev socat

WORKDIR /app

COPY . .
RUN gcc challenge.c -o challenge -fno-stack-protector -Wall
EXPOSE 1337

CMD socat tcp-l:1337,reuseaddr,fork EXEC:"./challenge",pty,stderr
