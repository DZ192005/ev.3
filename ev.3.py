while True:
    print('1.Registrar puntajes')
    print('2.Listar todos los puntajes')
    print('3.imprimir por tipo')
    print('4.Salir del programa')
    
    try:
        opc= int(input("Ingrese su opcion:\n--->"))
    except:
     id =input("ingrese su id a registrarse:")
    nombre=input("ingrese su nombre a registrarse:")
    apellido=input("ingrese su apellido a registrarse:")
    
    if opc== 1:
     opc1=print("1.Valorant")
     opc2=print("2.Fortnite")
     opc3=print("3.Fifa")

    if opc1 == opc2:
     Juegos=int(input('ingrese el juego que quiera resgristrarse:\n--->'))
    reg_puntajes=puntos
    reg_valorant=[]
    reg_fortnite=[]
    reg_fifa=[]
    puntos=int(input('ingrese puntos a registrarse'))
    reg_valorant=int(input('ingrese su punto a registrarse :'))
    reg_valorant=puntos
    reg_fortnite=int(input('ingrese su puntos a registrarse:'))
    reg_fortnite=puntos
    reg_fifa=int(input('ingrese su punto a registrarse:'))

    if opc==1:
      print("1.Principiante")
      print("2.Avazado")
      print("3.experto")
    try:
        categoria=int(input("ingrese su categoria:\n--->"))
        if categoria==1:
          categoria.append()
          





