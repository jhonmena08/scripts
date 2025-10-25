
import random, os

def main() -> int:
    frutas = ['🍊', '🍉', '🍒', '🍇']
    cant_frutas: int = len(frutas)

    display = list[str]
    counter: int = 1

    option = 'y'
    while option == 'y' or option == 'Y' or option == '':
        # seleccionar frutas al azar
        idx1: int = random.randint(0, cant_frutas - 1)
        idx2: int = random.randint(0, cant_frutas - 1)
        idx3: int = random.randint(0, cant_frutas - 1)

        # mostrar en pantalla
        os.system('cls')
        print(f'Intento No: {counter:02d}\n')
        print(f'| {frutas[idx1]} | {frutas[idx2]} | {frutas[idx3]} |\n')
        counter += 1

        if idx1 == idx2 == idx3:
            print('🎉🎉 Felicitaciones, ganaste !!!\n')
            break
        else:
            print('Perdiste !!, 😞 😞\n')

        option = input('Deseas seguir jugando ? [Y]: ')

    return 0



if __name__ == "__main__":
    main()
