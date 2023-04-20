from Mascota import mascota
from Dueño_mascota import dueño

if __name__ == "__main__":
    
    print("Ingrese datos del dueño de la mascota")
    nombre_dueño = input("Ingrese nombre del dueño: ")
    fecha_dueño = int(input("Ingrese fecha de nacimiento(sin puntos y guiones): "))
    ciudad_dueño = input("Ingrese ciudad de residencia: ")
    mascota_dueño = input("Ingrese nombre de la mascota: ")
    Dueño = dueño(nombre_dueño,fecha_dueño,ciudad_dueño,mascota_dueño)
    
    nombre_mascota = mascota_dueño
    especie = input("Ingrese especie de la mascota: ")
    raza = input("Ingrese raza del animal: ")
    fecha_nacimiento = input("Ingrese fecha de nacimiento de la mascota( de la misma forma que anteriormente): ")
    Mascota = mascota(nombre_mascota,especie,raza,fecha_nacimiento)
    
    def __repr__(self):
        return print("Datos del dueño son:", Dueño)
    
    print(f"Los datos del dueño son: {Dueño}, y de la mascota son {Mascota}")
    
    
    