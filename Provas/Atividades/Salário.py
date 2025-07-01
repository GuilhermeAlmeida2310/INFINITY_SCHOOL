salario = float(input('Insira seu Salário: '))
horas_semana = float(input('Insira suas Horas Semanais: '))
horas_mes = horas_semana * 4
ganho_por_hora = salario / horas_mes

print(f'Seu ganho por hora é de: {ganho_por_hora}')
