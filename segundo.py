def funcion1():
    print("Programa de Arioc - segundo.py")


if __name__ =='__main__':
    funcion1()
    print('segundo.py ejecutado directamente')

else:
    print(f"segundo.py fue importado. {__name__}")