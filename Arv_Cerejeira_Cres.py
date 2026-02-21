import turtle
import random

tela = turtle.Screen()
tela.bgcolor("skyblue")
tela.title("Árvore de Cerejeira Crescendo")
tela.tracer(0)

arvore = turtle.Turtle()
arvore.hideturtle()
arvore.speed(0)
arvore.color("brown")

petalas = turtle.Turtle()
petalas.hideturtle()
petalas.speed(0)
petalas.color("pink")
petalas.penup()

petalas_caindo = turtle.Turtle()
petalas_caindo.hideturtle()
petalas_caindo.speed(0)
petalas_caindo.penup()
petalas_caindo.color("pink")

posicoes_petalas = []

arvore.penup()
arvore.goto(0, -250)
arvore.setheading(90)
arvore.pendown()

pilha = []
pilha.append((arvore.pos(), arvore.heading(), 100, 0))  # pos, angulo, comprimento, etapa

def animarCrescimento():
    if not pilha:
        tela.update()
        animarPetalasCaindo()
        return

    pos, ang, comp, etapa = pilha.pop()

    arvore.penup()
    arvore.goto(pos)
    arvore.setheading(ang)

    if comp < 10:
        arvore.pendown()
        arvore.pensize(1)
        arvore.forward(comp)  
        petalas.goto(arvore.pos())
        petalas.dot(random.randint(6, 10), "pink")
        posicoes_petalas.append(arvore.pos())
        tela.update()
        tela.ontimer(animarCrescimento, 20)
        return

    if etapa == 0:
        arvore.pendown()
        arvore.pensize(comp / 10)
        arvore.forward(comp)
        novo_pos = arvore.pos()
        novo_ang = arvore.heading()

        angulo = random.randint(15, 25)
        encurtar = random.uniform(0.7, 0.85)

        pilha.append((novo_pos, novo_ang, comp, 1))  # recuar depois
        pilha.append((novo_pos, novo_ang + angulo * 2, comp * encurtar, 0))  # esquerdo
        pilha.append((novo_pos, novo_ang - angulo, comp * encurtar, 0))  # direito

    elif etapa == 1:
        arvore.pendown()
        arvore.pensize(comp / 10)
        arvore.backward(comp)

    tela.update()
    tela.ontimer(animarCrescimento, 20)

objetos = []
frame_atual = 0
total_frames = 60

def animarPetalasCaindo():
    global frame_atual, objetos

    if frame_atual == 0:
        objetos = [[x, y] for x, y in posicoes_petalas]

    petalas_caindo.clear()

    for i in range(len(objetos)):
        x, y = objetos[i]
        y -= random.uniform(2, 4)
        x += random.uniform(-1, 1)
        objetos[i] = [x, y]
        petalas_caindo.goto(x, y)
        petalas_caindo.dot(random.randint(4, 8), "pink")

    tela.update()
    frame_atual += 1
    if frame_atual < total_frames:
        tela.ontimer(animarPetalasCaindo, 40)

animarCrescimento()

tela.exitonclick()