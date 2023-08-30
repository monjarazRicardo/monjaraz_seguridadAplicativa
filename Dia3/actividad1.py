#verifica si una cadena es palindromo o no es palindromo
cadena = "Arenera"


if (cadena[::-1].lower() == cadena.lower()):

    print("Es palindromo")

else:
    print("No es palindromo")
    
