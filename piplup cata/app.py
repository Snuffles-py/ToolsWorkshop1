def calcular_promedio(notas):
    total = sum(notas)
    promedio = total / len(notas)
    return promedio

def main():
    print("--- Sistema de Promedios de Alumnos ---")
    
    alumnos = {
        "Dante": [2.0, 3.5, 5.1],
        "Lucas": [6.5, 7.0, 6.7],
        "Estudiante_Nuevo": [3.0, 5.0, 5.0] 
    }

    for nombre, notas in alumnos.items():
        try:
            p = calcular_promedio(notas)
            print(f"El promedio de {nombre} es: {p:.2f}")
        except Exception as e:
            print(f"⚠️ Error procesando a {nombre}: {e}")

if __name__ == "__main__":
    main()