#!/bin/python3

from datetime import datetime, timezone, timedelta

# Formatando datas e horários e transformando tudo em string.

data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')

print(data_e_hora_em_texto)

# Convertendo string em datetime.

data_e_hora_em_texto_2 = '01/03/2019 12:30'
data_e_hora = datetime.strptime(data_e_hora_em_texto_2, '%d/%m/%Y %H:%M')

print(data_e_hora)

# Fuso horário
# O parâmetro offset representa a diferença entre o fuso horário que queremos criar e o Tempo Universal Coordenado (UTC)

# Calcular a diferença de horários com a classe timedelta

diferenca = timedelta(hours=-3)
print(diferenca)

# Resolvendo o problema do fuso horário

fuso_horario = timezone(diferenca)
print(fuso_horario)

data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')

print(data_e_hora_sao_paulo_em_texto)
