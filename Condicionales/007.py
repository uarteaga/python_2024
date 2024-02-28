'''
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta	           Tipo impositivo
Menos de 10000$	          5%
Entre 10000$ y 20000$	  15%
Entre 20000$ y 35000$	  20%
Entre 35000$ y 60000$	  30%
Más de 60000$	          45%


'''


ingresos = int(input('Captura tus ingresos: '))

if ingresos <= 10000:
    impuesto = 5

elif ingresos <= 20000:
    impuesto = 15

elif ingresos <= 35000:
    impuesto = 20

elif ingresos <= 60000:
    impuesto = 30

else:
    ingresos > 60000
    impuesto = 30
    
print(f'Pagarás el {impuesto}% de impuestos')