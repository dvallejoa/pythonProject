def validar(c):
    print("La cadena introducida es:", c)
    x = True
    for i in c:
         if i=='A' or i=='C' or i=="T" or i=="G":
            print("Valor revisado:", i)
         else:
            print("\nWARNING 0001: Valor introducido no válido")
            print("WARNING 0001:", i)
            break

def main():
    cad  = input("Introduce la cadena: ")
    validar(cad)


if __name__ == "__main__":
    main()