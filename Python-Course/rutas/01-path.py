from pathlib import Path

# Path(r"C:\Archivos de Programa\Minecarft")
# Path("/usr/bin")
# Path()
# Path.home()
# Path("one/__ini__.py")

path = Path("hola-mundi/mi-archivo.py")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute()
)

p = path.with_name("chanchito.py")
