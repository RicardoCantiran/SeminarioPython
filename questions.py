import random
# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
("size()", "len()", "length()", "count()"),
("3.14", "'42'", "10", "True"),
("input()", "scan()", "read()", "ask()"),
(
    "// Esto es un comentario",
    "/* Esto es un comentario */",
    "-- Esto es un comentario",
    "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]

# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

# El usuario deberá contestar 3 preguntas
puntos = 0.0
questions_to_ask = random.choices(list(zip(questions,answers, correct_answers_index)), k=3)
for questions, answers, question_index in questions_to_ask:
    # Se selecciona una pregunta aleatoria
    # Se muestra la pregunta y las respuestas posibles
    print(questions)
    for i, answer in enumerate(answers):
        print(f"{i + 1}. {answer}")
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        respuesta = input("Respuesta ")

        #compruebo que sea un numero y que este a rango de las preguntas
        if(respuesta.isdigit() and int(respuesta) > 0 and int(respuesta) < 5 ):
            respuesta = int(respuesta) -1
        else:
            #sino fuerzo un cierre del programa con exit
            print ("respuesta invalida")
            exit(1)
        #Se verifica si la respuesta es correcta
        if respuesta == question_index:
            print("¡Correcto!")
            puntos += 1.0
            break
        else:
            puntos -= 0.5
    else:
        # Si el usuario no responde correctamente después de 2 intentos, # se muestra la respuesta correcta
         print("Incorrecto. La respuesta correcta es:")
         print(answers[question_index])
# Se imprime un blanco al final de la pregunta
    print()
print("su puntaje en el juego fue de :", puntos )
