# Backup Manager

Estamos en el mundo de la informática, lugar en el que errores humanos y tecnológicos forman parte de nuestro día a día y tenemos que vivir con ellos. Es necesario tomar precauciones para que estos errores no se cometan tanto, pero es seguro que se van a cometer. Por ello, se ha desarrollado la herramienta Backup Manager, que se ejecuta en el servidor, creando automáticamente una carpeta de backup de la carpeta que hayamos seleccionado.

Un uso que podría tener es, mediante un crontab, exportar periódicamente una copia de una base de datos, en su carpeta correspondiente, y después, con el crontab también, ejecutar Backup Manager para tener la copia de seguridad. 
Backup Manager utiliza un script de python para generar la copia de la carpeta, y el posicionamiento en el nuevo lugar.
