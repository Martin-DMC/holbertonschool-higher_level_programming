#!/usr/bin/python3
"""
this script create a simple templating program.

1 - toma la plantilla template.txt
2 - definir los datos, con la lista proporcionada.
3 - definir la funcion donde ocurre la magia
4 - verificar inputs y plantilla, todo debe ser str
5 - verificar entradas vacias, asistentes o plantilla y devolver mensaje
6 - fusionar datos con los mascadores en la
    plantilla, si no hay dato remplazar con n/a
7 - generar las invitaciones en output_x.txt
    donde 'x' es el indice de invitados
"""
import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: la plantilla debe ser una cadedna de texto")
        return

    if not isinstance(attendees, list):
        print("Error: es necesario una lista de diccionarios")
        return

    if not template:
        print("Error: es necesario una plantilla")
        return

    if not attendees:
        print("Error: es necesario una lista de invitados")
        return

    if not os.path.exists(template):
        print("Error: la plantilla no fue encontrada")
        return

    try:
        with open(template, "r") as plantilla:
            copia = plantilla.read()
    except IOError as e:
        print(f"Error al leer la plantilla: {e}")
        return

    for i, datos in enumerate(attendees):
        name = datos.get('name', 'N/A')
        if name is None:
            name = 'N/A'
        event = datos.get('event_title', 'N/A')
        if event is None:
            event = 'N/A'
        date = datos.get('event_date', 'N/A')
        if date is None:
            date = 'N/A'
        location = datos.get('event_location', 'N/A')
        if location is None:
            location = 'N/A'
        with_name = copia.replace('{name}', name)
        with_event = with_name.replace('{event_title}', event)
        with_date = with_event.replace('{event_date}', date)
        new_plantilla = with_date.replace('{event_location}', location)
        try:
            with open(f"output_{i}.txt", "w") as archivo:
                archivo.write(new_plantilla)
        except IOError as e:
            print(f"Error al escribir la invitacion: {e}")
        except Exception as e:
            print(f"Error inesperado al generar archivo: {e}")

