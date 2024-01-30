'''
002 function example
función que sume dos números


def suma_dos(num_uno, num_dos):
    resultado = int(num_uno) + int(num_dos)
    return resultado

print(suma_dos(5,2))
'''

def team(team_name):
    return f'El nombre del equipo es: {team_name}'

#print(team('Oracle Red Bull Racing'))

def drivers(team, driver_one, driver_two):
    return f'{team}. Los pilotos son: {driver_one} y {driver_two}'

#team = team("Red Bull")
#print(drivers(team, "Max Verstappen", "Sergio Pérez"))

#print(drivers(team('Ferrari'), "Max Verstappen", "Sergio Pérez"))

user_team = input("team name: ")
input_team = team(user_team)
team_pilot_one = input("piloto uno: ")
team_pilot_two = input("piloto dos: ")

print(drivers(input_team, team_pilot_one, team_pilot_two))