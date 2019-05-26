def capitales():

    aciertos = 0
    errores = 0

    capitales = {'Francia': 'Paris', 'Bielorusia': 'Minsk', 'Malta': 'La Valeta', 'Suiza': 'Berna' }

    for pareja in capitales.keys():
        pais = input('Cúal es la capital de '+ pareja +' : ')

        if pais.upper() == capitales[pareja].upper():
            print('Bene')
            aciertos += 1

        else:
            print('Niente')
            seguimos = input('Mira que era sencillo,  quiéres seguir S/N: ')
            errores += 1

            if seguimos.upper() == 'N':
                print('Mejor dejarlo si')
                break

    print('\nAcertaste: ', aciertos)
    print("Fallaste:", errores)
    print('Hasta luego Lucas')

capitales()