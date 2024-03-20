from lessons import (
    init,
    lesson1,
    lesson2,
    lesson3,
    lesson4,
    lesson5,
    lesson6,
    lesson7,
    lesson8,
    lesson9,
    lesson10,
    lesson11,
    lesson12,
    lesson13,
    lesson14,
    lesson15,
)


exercicios = [
    init,
    lesson1,
    lesson2,
    lesson3,
    lesson4,
    lesson5,
    lesson6,
    lesson7,
    lesson8,
    lesson9,
    lesson10,
    lesson11,
    lesson12,
    lesson13,
    lesson14,
    lesson15,
]

print("Olá meus caros amigos")
input("Pressione Enter para começar os exercícios...")

if input() == "":
    for exercicio in exercicios:
        input("Pressione Enter para continuar...")
        exercicio.main()
else:
    print("Você precisa pressionar Enter para começar os exercícios.")
