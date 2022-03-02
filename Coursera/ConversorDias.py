Segundos = int(input("Por favor, entre com o numero de segundos que deseja converter: "))

Dias = Segundos // 86400 # ((60*60)*24) Segundos*Minutos*Hooras 
Resto = Segundos % 86400

Horas = Resto // 3600 # (60*60) Segundos*Minutos
Resto = Segundos % 3600

Minutos = Resto // 60 # Segundos
Segundos = Segundos % 60

print(Dias,"dias,",Horas,"horas,",Minutos, "minutos,",Segundos,"segundos.")
