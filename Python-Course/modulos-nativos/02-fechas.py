# import time

# print(time.time())

from datetime import datetime

fecha = datetime(2025, 2, 21)
fecha2 = datetime(2025, 2, 21)

ahora = datetime.now()
fechaStr = datetime.strptime("2023-01-03", "%Y-%m-%d")
print(fecha.strftime("%Y.%m.%d"))
