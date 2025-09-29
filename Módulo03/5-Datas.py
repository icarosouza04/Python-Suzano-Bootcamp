# Lidando com data, hora e fuso horário no Python

from datetime import date, datetime, time, timedelta, timezone

data = date(2025, 9, 28)

print(data)

print(date.today()) # Exibe a data atual

data_hora = datetime(2025, 9, 28) # O horário deve ser passado por parâmetro

print(data_hora)

print(datetime.today()) # Exibe a data e o horário atual

hora = time(18, 30, 0) # Exibe o horário informado

print(hora)

# timedelta

tipo_carro = "P"
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":

    data_estimada = data_atual + timedelta(minutes = tempo_pequeno)

    print(f"O carro chegou {data_atual} e ficará pronto às {data_estimada}.")

elif tipo_carro == "M":

    data_estimada = data_atual + timedelta(minutes = tempo_medio)

    print(f"O carro chegou {data_atual} e ficará pronto às {data_estimada}.")

else:

    data_estimada = data_atual + timedelta(minutes = tempo_grande)

    print(f"O carro chegou {data_atual} e ficará pronto às {data_estimada}.")

resultado = datetime(2025, 9, 28, 20, 9, 0) - timedelta(hours = 1)

print(resultado.time())

print(datetime.now().date())

# Formatando e convertendo datas com strftime e srtptime

data_hora_atual = datetime.now()
data_hora_str = "2025-09-28 23:25"
mascara_ptbr = "%d/%m/%Y"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))

data_convertida = (datetime.strptime(data_hora_str, mascara_en))

print(data_convertida)
print(type(data_convertida))

# pytz e timezone

import pytz

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data)
print(data2)

# Solução sem pytz

data_oslo = datetime.now(timezone(timedelta(hours = 2)))
data_sao_paulo = datetime.now(timezone(timedelta(hours = -3)))

print(data_oslo)
print(data_sao_paulo)
