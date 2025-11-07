# Atividade 03.
# Crie um programa que permite ao usuário calcular a área e o perímetro de formas geométricas simples, como quadrados, retângulos e círculos. Use funções matemáticas do módulo math para realizar os cálculos.

import math


def quadrado(lado):
    area = lado ** 2
    perimetro = 4 * lado
    return area, perimetro


def retangulo(largura, altura):
    area = largura * altura
    perimetro = 2 * (largura + altura)
    return area, perimetro


def circulo(raio):
    area = math.pi * raio ** 2
    perimetro = 2 * math.pi * raio
    return area, perimetro
