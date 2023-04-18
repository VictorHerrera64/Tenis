import os

jugador1 = {'nombre':''}
jugador2 = {'nombre':''}
tenis = {'j1':None,'j2':None,'marcador_j1':0,'marcador_j2':0,'set_j1':0,'set_j2':0,'set_tenis':0}
puntajes = [0,15,30,40,50]
contador1 = 1
contador2 = 1
continuaMenu = 1
while continuaMenu==1:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------------------")
    print("------   Menu  --------")
    print("-----------------------")
    print("1) Configurar jugadores")
    print("2) Empezar el juego")
    print("-----------------------")
    opcion=int(input("Ingrese una opcion : "))
    if opcion==1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--------Configuracion Jugador 1---------")
        jugador1['nombre']=input("Ingrese un nombre a jugador 1 : ")
        if(jugador1['nombre'] == ''):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("------ Error -------")
            jugador1['nombre']=input("Ingrese un nombre a jugador 1 : ")
        print("--------Configuracion Jugador 2---------")
        jugador2['nombre']=input("Ingrese un nombre a jugador 2 : ")
        if(jugador2['nombre'] == ''):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("------ Error -------")
            jugador2['nombre']=input("Ingrese un nombre a jugador 2 : ")
        nombre_j1 = jugador1['nombre']
        nombre_j2 = jugador2['nombre']
        os.system('cls' if os.name == 'nt' else 'clear')
        print("CONFIGURACION")
        print(f'Jugador 1 : {nombre_j1}')
        print(f'Jugador 2 : {nombre_j2}')
        tenis = {'j1':jugador1,'j2':jugador2,'marcador_j1':None,'marcador_j2':None,'ganador':None}
        print("-----------------------")
    elif opcion==2:
        if(jugador1['nombre'] == '' and jugador2['nombre'] ==''):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("-----------------------------------------------")
            print("------ Error Configuracion de Jugador ---------")
            print("Primero debe escribir un nombre a los jugadores")
            print("-----------------------------------------------")
        else:
            print("-------- Inicio Partido de Tenis ---------")
            p1 = jugador1['nombre']
            p2 = jugador2['nombre']
            marcador1 = 0
            marcador2 = 0
            setj1 = 0
            setj2 = 0
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'MARCADOR (JUEGO ACTUAL)')
                print(f'Jugador 1: {p1} ->  [{marcador1}] - [{marcador2}] <- Jugador 2: {p2}')
                print(f'MARCADOR (GLOBAL)')
                print(f'Juegos Ganados ({p1}): [{setj1}] - [{setj2}] Juegos Ganados: ({p2})')
                print(' |////////////////////////////////////////////////////////////|')
                print(f'Jugador 1 anota punto? ')
                point1=int(input(" 1) Si \n 2) No \n Respuesta : "))
                if(point1==1):
                    marcador1 = puntajes[contador1] 
                    tenis['marcador_j1'] = marcador1
                    contador1+=1
                else:
                    pass
                print(' |////////////////////////////////////////////////////////////|')
                print(f'Jugador 2 anota punto? ')
                point2=int(input(" 1) Si \n 2) No \n Respuesta : "))
                if(point2==1):
                    marcador2 = puntajes[contador2] 
                    contador2+=1
                    tenis['marcador_j2'] = marcador2
                else:
                    pass
                marcador1 = tenis['marcador_j1']
                marcador2 = tenis['marcador_j2']
                
                if(contador1 == 5):
                    setj1 +=1
                    tenis['set_j2']= setj1
                    contador1 = 1
                    contador2 = 1
                    marcador1 = puntajes[0]
                    marcador2 = puntajes[0]
                    tenis['marcador_j1'] = marcador1
                    tenis['marcador_j2'] = marcador2
                    if(setj1 == 7):
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'EL JUGADOR 1: {p1} GANÓ LA PARTIDA DE TENIS')
                        print(f'MARCADOR (GLOBAL)')
                        print(f'Juegos Ganados ({p1}): [{setj1}] - [{setj2}] Juegos Ganados: ({p2})')
                        print("-------- Fin partido de Tenis ------------")
                        break
                    continue
                if(contador2 == 5):
                     setj2 +=1
                     tenis['set_j2']= setj2
                     contador1 = 1
                     contador2 = 1
                     marcador1 = puntajes[0]
                     marcador2 = puntajes[0]
                     tenis['marcador_j1'] = marcador1
                     tenis['marcador_j2'] = marcador2
                     if(setj2 == 7):
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'       EL JUGADOR 2: {p2} GANÓ LA PARTIDA DE TENIS     ')
                        print(f'MARCADOR (GLOBAL)')
                        print(f'Juegos Ganados ({p1}): [{setj1}] - [{setj2}] Juegos Ganados: ({p2})')
                        print("-------- Fin partido de Tenis ------------")
                        break
                     continue
    print("¿Desea realizar una nueva operación del menú? \n Opciones \n 1) Si \n 2) No")
    print("-----------------------")
    continuaMenu=int(input("Ingrese una opcion : "))
    os.system('cls' if os.name == 'nt' else 'clear')
    if continuaMenu != 1:
        print("Adios!")
   

