# Your_fist_weird_machine
## Categoria: pwn

¿Tal vez esas clases de ensamblador sirvieron para algo?
Formato de la bandera: flag{t3xto-de-ejempl0}

Instrucciones:
- Este setup imita la situación de un servidor remoto, de forma local. Para que sea realista, **NO PUEDES** ver el contenido de los archivos en la carpeta `SECRETO`.
- Para iniciar el contenedor con docker compose, usa `docker compose up -d`.
- Puedes conectarte al servicio expuesto con `nc localhost 1337`.
- Para finalizar el contenedor, usa `docker compose down`.

Tips:
- Puedes usar `objdump` para desensamblar el ejecutable y hacer un análisis estático.
- Puedes usar un debugger como `gdb` para hacer un análisis dinámico/estático.

