#!/bin/bash
figlet "SPORT OS"| lolcat
echo "Esta es la bash del sistema operativo SportOS, podrás ejecutar comandos relacionados con el mundo de los deportes. 
        Para comenzar, escribe el comando 'ayuda' para ver una lista de comandos disponibles.
        echo Prueba los comandos especiales 'futbol', 'baloncesto' y 'f1'. 
        Si deseas salir de la bash, escribe 'salir'.
        ¡Que disfrutes de tu experiencia en SportOS!"
echo "Lista de comandos disponibles:
        - ayuda: Muestra una lista de comandos disponibles.
   	    - abrir: Para abrir un archivo.
        - futbol: Muestra los mejores equipos de futbol.
        - baloncesto: Muestra los mejores equipos de baloncesto.
        - f1: Muestra las mejores escuderias de Formula 1.
        - matar-proceso: Mata un proceso.
        - web: Para obtener más información en nuestra página web.
        - salir: Sale de la bash.
        - crear: Crea un archivo.
        - eliminar: Elimina un archivo.
        - mover: Mueve un archivo.
        - copiar: Copia un archivo.
        - renombrar: Renombra un archivo.
        - buscar: Busca un archivo.
        - listar: Lista los archivos de un directorio.
        - limpiar: Limpia la pantalla.
        - escribir: Escribe un archivo."

while true; do
    echo -n "$USER@SportOS:~$ "  # Prompt personalizado
    read comando

    case $comando in
        ayuda)
            echo "Lista de comandos disponibles:
                    - ayuda: Muestra una lista de comandos disponibles.
                    - salir: Sale de la bash.
                    - crear: Crea un archivo.
                    - eliminar: Elimina un archivo.
                    - mover: Mueve un archivo.
                    - copiar: Copia un archivo.
                    - renombrar: Renombra un archivo.
                    - buscar: Busca un archivo.
                    - listar: Lista los archivos de un directorio.
                    - limpiar: Limpia la pantalla.
                    - web: Para obtener más información en nuestra página web."
        ;;
        abrir)
            echo "Que archivo quieres abrir?"
            read archivo
            nano "$archivo"
        ;;
        futbol)
            echo "⚽ Mejores equipos de fútbol de la actualidad ⚽"
            echo "--------------------------------------------"
            echo "1️⃣  FC Barcelona"
            echo "2️⃣  Bayern Múnich"
            echo "3️⃣  Real Madrid"
            echo "4️⃣  Manchester City"
            echo "5️⃣  Arsenal"
            echo "6️⃣  Paris Saint-Germain"
            echo "7️⃣  Liverpool"
            echo "8️⃣  Inter de Milán"
            echo "9️⃣  Atlético de Madrid"
            echo "🔟  Napoli"
            echo "--------------------------------------------"
        ;;

        baloncesto)
            echo "🏀 Mejores equipos de baloncesto de la actualidad🏀"
            echo "--------------------------------------------"
            echo "1️⃣  Milwaukee Bucks"
            echo "2️⃣  Denver Nuggets"
            echo "3️⃣  Boston Celtics"
            echo "4️⃣  Phoenix Suns"
            echo "5️⃣  Golden State Warriors"
            echo "6️⃣  Philadelphia 76ers"
            echo "7️⃣  Los Angeles Lakers"
            echo "8️⃣  Miami Heat"
            echo "9️⃣  Memphis Grizzlies"
            echo "🔟  Toronto Raptors"
            echo "--------------------------------------------"
        ;;

        f1)
            echo " Mejores equipos de la Fórmula 1 de la actualidad"
            echo "--------------------------------------------"
            echo "1️⃣  Red Bull Racing"
            echo "2️⃣  Mercedes-AMG Petronas"
            echo "3️⃣  Ferrari"
            echo "4️⃣  Aston Martin"
            echo "5️⃣  McLaren"
            echo "6️⃣  Alpine"
            echo "7️⃣  Alfa Romeo"
            echo "8️⃣  Haas F1 Team"
            echo "9️⃣  AlphaTauri"
            echo "🔟  Williams Racing"
            echo "--------------------------------------------"
        ;;

        matar-proceso)
            echo "Escribe el nombre del proceso que deseas matar:"
            read proceso
            kill -9 "$proceso"
            echo "¡Proceso $proceso eliminado!"
        ;;

        web)
            firefox file:///home/Alex/Desktop/pagina.html/Principal.HTML
        ;;

        salir)
            echo "¡Hasta luego!"
            exit
        ;;

        crear)
            echo "Escribe el nombre del archivo que deseas crear:"
            read archivo
            touch "$archivo"
            echo "¡Archivo $archivo creado!"
        ;;

        eliminar)
            echo "Escribe el nombre del archivo que deseas eliminar:"
            read archivo
            rm "$archivo"
            echo "¡Archivo $archivo eliminado!"
        ;;

        mover)
            echo "Escribe el nombre del archivo que deseas mover:"
            read archivo
            echo "Escribe la dirección de destino:"
            read destino
            mv "$archivo" "$destino"
            echo "¡Archivo $archivo movido a $destino!"
        ;;

        copiar)
            echo "Escribe el nombre del archivo que deseas copiar:"
            read archivo
            echo "Escribe la dirección de destino:"
            read destino
            cp "$archivo" "$destino"
            echo "¡Archivo $archivo copiado a $destino!"
        ;;

        renombrar)
            echo "Escribe el nombre del archivo que deseas renombrar:"
            read archivo
            echo "Escribe el nuevo nombre del archivo:"
            read nuevo
            mv "$archivo" "$nuevo"
            echo "¡Archivo $archivo renombrado a $nuevo!"
        ;;

        buscar)
            echo "Escribe el nombre del archivo que deseas buscar:"
            read archivo
            find . -name "$archivo"
        ;;

        listar)
            echo "Archivos del directorio actual:"
            ls -l
        ;;

        limpiar)
            clear
        ;;

        escribir)
            echo "Escribe el nombre del archivo en el que vas a escribir:"
            read archivo
            echo "¿Deseas abrir un editor de texto para escribir en el archivo? (s/n)"
            read respuesta
                if [ "$respuesta" = "s" ]; then
                    nano "$archivo"
                else
                    echo "Escribe el texto que deseas añadir al archivo:"
                    read texto
                    echo "$texto" >> "$archivo"
                fi
        ;;
        *)
            $comando 2>/dev/null || echo "Comando no reconocido. Escribe 'ayuda' para ver los comandos disponibles."
        ;;
	esac 
done