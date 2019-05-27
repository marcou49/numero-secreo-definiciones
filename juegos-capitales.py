def capitales():

    aciertos = 0
    errores = 0

#creamos diccionario de paises:capitales
    capitales = {'Francia': 'Paris', 'Bielorusia': 'Minsk', 'Malta': 'La Valeta', 'Suiza': 'Berna' }

    for pareja in capitales.keys():
        pais = input('Cúal es la capital de '+ pareja +' : ')

        if pais.upper() == capitales[pareja].upper(): #el usuario acierta sumamos un acierto
            print('Bene')
            aciertos += 1

        else:
            print('Niente')
            errores += 1 #error del usuario sumamos un error y le preguntamos si quier seguir

         

    print('\nAcertaste: ', aciertos)
    print("Fallaste:", errores)
    print('Hasta luego Lucas')

capitales()
