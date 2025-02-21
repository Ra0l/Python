from pathlib import Path
import sys


def cli(args):
    if len(args) == 1:
        print("no se pasaron argumentos")
        return
    if len(args) != 3:
        print("Se necesitan 2 argumentos")

    origen = args[1]
    o = Path(origen)
    if not o.exists():
        print("Origen no existente")
        return


cli(sys.argv)
