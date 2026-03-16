frutas = ("maçã", "banana", "laranja", "uva", "manga")

print("Frutas disponíveis na feira:")
for fruta in frutas:
    print("-", fruta)

consulta = input("Digite o nome de uma fruta para verificar se está disponível: ").lower()
if consulta in frutas:
    print(f"{consulta.capitalize()} está disponível na feira!")
else:
    print(f"{consulta.capitalize()} não está disponível na feira.")

print(f"Total de frutas disponíveis: {len(frutas)}")