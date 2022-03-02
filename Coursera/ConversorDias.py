Segundos = int(input("Por favor, entre com o numero de segundos que deseja converter: "))
Dias = Segundos // 24
Segundos = Segundos % 24

Horas = Segundos// (60*60)
Segundos = Segundos % (60*60)

Minutos = Segundos // 60
Segundos = Segundos % 60

print(Dias,"dias,",Horas,"horas,",Minutos, "minutos,",Segundos,"segundos.")
