import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def generar_temperaturas(num_ciudades, num_dias_semana, num_semanas):
    """
    Genera una matriz 3D de temperaturas aleatorias entre -10 y 35 grados Celsius.
    :param num_ciudades: Número de ciudades.
    :param num_dias_semana: Número de días en la semana.
    :param num_semanas: Número de semanas.
    :return: Matriz 3D de temperaturas.
    """
    np.random.seed(0)  # Para reproducibilidad
    temperaturas = np.random.uniform(low=-10, high=35, size=(num_ciudades, num_dias_semana, num_semanas))
    return temperaturas


def calcular_promedios_semanales(temperaturas):
    """
    Calcula el promedio de temperaturas para cada ciudad y semana.
    :param temperaturas: Matriz 3D de temperaturas.
    :return: Matriz 2D de promedios semanales.
    """
    num_ciudades, num_dias_semana, num_semanas = temperaturas.shape
    promedios_semanales = np.zeros((num_ciudades, num_semanas))

    for ciudad in range(num_ciudades):
        for semana in range(num_semanas):
            temperaturas_semana = temperaturas[ciudad, :, semana]
            promedio_semana = np.mean(temperaturas_semana)
            promedios_semanales[ciudad, semana] = promedio_semana

    return promedios_semanales


def animar(i):
    """
    Actualiza la animación para el frame i.
    :param i: Número del frame actual.
    """
    plt.clf()
    plt.title(f'Promedio de Temperaturas - Semana {i + 1}')
    for ciudad in range(num_ciudades):
        plt.plot(range(1, i + 2), promedios_semanales[ciudad, :i + 1], label=f'Ciudad {ciudad + 1}')
    plt.xlabel('Semanas')
    plt.ylabel('Temperatura Promedio (°C)')
    plt.legend()
    plt.grid(True)


def main():
    global num_ciudades, promedios_semanales

    num_ciudades = 4
    num_dias_semana = 7
    num_semanas = 4

    # Generar temperaturas
    temperaturas = generar_temperaturas(num_ciudades, num_dias_semana, num_semanas)

    # Calcular promedios semanales
    promedios_semanales = calcular_promedios_semanales(temperaturas)

    # Mostrar los resultados en la consola
    for ciudad in range(num_ciudades):
        for semana in range(num_semanas):
            print(
                f'Ciudad {ciudad + 1}, Semana {semana + 1}: Promedio de temperatura = {promedios_semanales[ciudad, semana]:.2f}°C')

    # Configurar la animations
    fig = plt.figure()
    ani = animation.FuncAnimation(fig, animar, frames=num_semanas, repeat=False)
    plt.show()


if __name__ == "__main__":
    main()
