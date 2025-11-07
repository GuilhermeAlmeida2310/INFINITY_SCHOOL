# Atividade 1.
# Crie uma função que receba um nome e imprima uma saudação personalizada.

def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a)!")
saudacao("Guilherme")

# Atividade 2.
# Crie uma função que receba um horário e imprima "Bom dia!","Boa tarde!"ou"Boa noite!"conforme o horário.

def saudacao_horario(horario):
    if 6 <= horario < 12:
        print('Bom dia')
    elif 12 <horario <18:
        print('Boa tarde')
    else:
        print('Boa noite')
saudacao_horario(4)

# Atividade 3.
# Crie uma função que receba dois números e retorne a soma deles.

def soma(num1,num2):
    return num1 + num2
print(soma(5,5))

# Atividade 4.
# Crie uma função que receba dois números e retorne a subtração do primeiro pelo segundo.

def subtracao(num1,num2):
    print(subtracao(10,5))
    return num1 - num2

# Atividade 5.
# Crie uma função que receba dois números e retorna a multiplicação deles.

def subtracao(num1,num2):
    return num1 * num2
print(subtracao(10,5))

