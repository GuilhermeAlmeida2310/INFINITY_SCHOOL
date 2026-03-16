# Sistema de Cadastro de Funcionário

# Passos:
# 1. Coletar dados
# 2. Processamento dos dados: Verificar maioridade e Calcular salário anual
# 3. Exibição do relatório

print("CADASTRO DE FUNCIONÁRIO")
nome = input("Digite o nome completo: ")
idade = int(input("Digite a idade: "))
salario_mensal = float(input("Digite o salário mensal (R$): "))

maior_idade = idade >= 18

salario_anual = salario_mensal * 12

print("RELATÓRIO DO FUNCIONÁRIO")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")

if maior_idade:
    print("Status: Maior de idade")
else:
    print("Status: Menor de idade")

print(f"Salário mensal: R$ {salario_mensal:.2f}")
print(f"Salário anual: R$ {salario_anual:.2f}")

print("Cadastro concluído com sucesso!")