import hashlib

hash_file = "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"

dic_file = input("Ingrese la dirección del archivo del diccionario: ")

with open(dic_file, 'r') as file:

    diccionario = [line.strip() for line in file] 

    for password in diccionario:

        hash_calculado = hashlib.sha256(password.encode()).hexdigest()

        if hash_calculado == hash_file:

            print("La contraseña original es: " + password)
            break
        
        else:
            print("La contraseña no se encuentra en el diccionario.")
    