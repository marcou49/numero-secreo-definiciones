import datetime
import json
import random


# pasamos la fecha al formato europeo solo con dia / mes / año
fecha = datetime.date.today()
hoy = fecha.strftime('%d-%b-%Y')

#definimos el juego
def jugar():

    nombre = input("Empezemos. Cómo te llamas ")
    secreto = random.randint(1, 5)
    intentos = 0
    score_list = get_score_list()

    while True:
        guess = int(input(" Pon un número del 1 al 30: "))
        intentos += 1

        if guess == secreto:
            score_list.append({"Intentos": intentos, "Fecha": hoy, "Nombre": nombre })

            with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("Bingo efectivamente es " + str(secreto) + ". Lo encontraste en " + str(intentos) + " intentos \n")
            break

        elif guess > secreto:
            print("No, menos")

        elif guess < secreto:
            print("No, más")




#lista de resultados

def get_score_list():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list


#lista de 3 mejores resultados

def get_top_scores():
    score_list = get_score_list()
    new_score_list = sorted(score_list, key=lambda k: k['Intentos'])[:3]
    return new_score_list



# lanzando el juego
while True:
    selection = input("Hola, teclea J para jugar, P para ver el palmares y Q para cerrar el juego ")

    if selection.upper() == "J":
        jugar()
    elif selection.upper() == "P":
        for score_dict in get_top_scores():

            score_text = "{0} encontro en {1} intentos el {2}.".format(score_dict.get("Nombre"),
                                                                       str(score_dict.get("Intentos")),
                                                                       score_dict.get("Fecha"))

            print(score_text)


    else:
        print('Hasta luego Lucas')
        break

