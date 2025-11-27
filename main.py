# main.py
#
# Archivo de ayuda para probar el proyecto localmente o en un entorno de ejecución.
# NOTA: freeCodeCamp solo usa RPS.py, pero esto te sirve para asegurar que todo anda.

from RPS import player
from RPS_game import play, quincy, abbey, kris, mrugesh

# Ejemplos de partidas
if __name__ == "__main__":
    print("Jugando contra quincy...")
    play(player, quincy, 1000, verbose=False)

    print("Jugando contra abbey...")
    play(player, abbey, 1000, verbose=False)

    print("Jugando contra kris...")
    play(player, kris, 1000, verbose=False)

    print("Jugando contra mrugesh...")
    play(player, mrugesh, 1000, verbose=False)

    # Descomentar la siguiente línea si querés correr los tests desde acá
    # import test_module
    # test_module.test()
