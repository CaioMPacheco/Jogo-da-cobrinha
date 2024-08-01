import pygame
from pygame.locals import *
from sys import exit
from random import randint

#começo

pygame.init()

pygame.mixer_music.set_volume(0.2)
musica_fundo = pygame.mixer_music.load("Musicas/Game Over - Super Mario World Remix-mc.mp3")
pygame.mixer.music.play(-1)

barulho_perdeu = pygame.mixer.Sound("Musicas/smw_lost_a_life.wav")
barulho_perdeu.set_volume(0.5)
barulho_colisão = pygame.mixer.Sound('Musicas/smw_coin.wav')

largura = 800
altura = 600

x_cobra = int(largura/2  - 20/2)
y_cobra = int(altura/2 - 20/2)

velocidade = 5
x_controle = velocidade
y_controle = 0

fonte = pygame.font.SysFont('Times', 40, True, True)
pontos = 0

x_maça = randint(40, 600)
y_maça = randint(50, 430)
clock = pygame.time.Clock()

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("BomberMan, by Caio")

lista_cobra = []
comprimento = 5

morreu = False

#Código

def aumenta_corpo(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20, 20))

def reiniciar_jogo():
    global pontos, comprimento, x_cobra, y_cobra, lista_cobra, lista_cabeça, velocidade, x_maça, y_maça, morreu
    pontos = 0
    comprimento = 5
    x_cobra = int(largura/2  - 20/2)
    y_cobra = int(altura/2 - 20/2)
    lista_cobra = []
    lista_cabeça = []
    velocidade = 5
    x_maça = randint(40, 600)
    y_maça = randint(50, 430)
    morreu = False


while True:
    clock.tick(60)
    tela.fill((255,255,255))
    mensagem = f'Pontos: {pontos}'
    text_formatado = fonte.render(mensagem, True, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
       
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle

    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra, y_cobra,20,20))
    maça = pygame.draw.circle(tela, (255,0,0), (x_maça, y_maça,), 10)

    if cobra.colliderect(maça):
        x_maça = randint(40,600)
        y_maça = randint(50, 430)
        pontos += 1
        barulho_colisão.play()
        comprimento += 1
        velocidade += 0.001

    lista_cabeça = []
    lista_cabeça.append(x_cobra)
    lista_cabeça.append(y_cobra)
    lista_cobra.append(lista_cabeça)

    if lista_cobra.count(lista_cabeça) > 1:
        mensagem2 = f'Você perdeu, comece novamente!'
        mensagem3 = f'Aperte a tecla R!'
        text_formatado2 = fonte.render(mensagem2, True, (0, 0, 0))
        text_formatado3 = fonte.render(mensagem3, True, (0, 0, 0))
        morreu = True
        barulho_perdeu.play()
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            tela.blit(text_formatado2, (20, 200))
            tela.blit(text_formatado3, (20, 280))
            pygame.display.update()

    if x_cobra  > largura or x_cobra < 0:
        mensagem2 = f'Você perdeu, comece novamente!'
        mensagem3 = f'Aperte a tecla R!'
        text_formatado2 = fonte.render(mensagem2, True, (0, 0, 0))
        text_formatado3 = fonte.render(mensagem3, True, (0, 0, 0))
        morreu = True
        barulho_perdeu.play()
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            tela.blit(text_formatado2, (20, 200))
            tela.blit(text_formatado3, (20, 280))
            pygame.display.update()
        
    if y_cobra  > altura or y_cobra < 0:
        mensagem2 = f'Você perdeu, comece novamente!'
        mensagem3 = f'Aperte a tecla R!'
        text_formatado2 = fonte.render(mensagem2, True, (0, 0, 0))
        text_formatado3 = fonte.render(mensagem3, True, (0, 0, 0))
        morreu = True
        barulho_perdeu.play()
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            tela.blit(text_formatado2, (20, 200))
            tela.blit(text_formatado3, (20, 280))
            pygame.display.update()

    if len(lista_cobra) > comprimento:
        del lista_cobra[0]

    aumenta_corpo(lista_cobra)

    tela.blit(text_formatado, (400, 400))
    pygame.display.update()