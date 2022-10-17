import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.1)
musica_de_fundo = pygame.mixer.music.load('BoxCat Games - Mt Fox Shop.mp3')
barulho_colisao = pygame.mixer.Sound('smw_1-up.wav')
pygame.mixer.music.play(-1)


largura = 850
altura = 650
x = largura / 2
y = altura / 2

x_azul = randint(40, 600)
y_azul = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, bold=True, italic=True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("jogo pablo")
velocidade = pygame.time.Clock()

while True:
    velocidade.tick(50)
    tela.fill((0, 0, 0))

    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        # if event.type == KEYDOWN:
        #     if event.key == K_a:
        #         x = x - 20
        #     if event.key == K_d:
        #         x = x + 20
        #     if event.key == K_z:
        #         y = y + 20
        #     if event.key == K_s:
        #         y = y - 20

        if pygame.key.get_pressed()[K_a]:
            x = x - 20
        if pygame.key.get_pressed()[K_d]:
            x = x + 20
        if pygame.key.get_pressed()[K_s]:
            y = y - 20
        if pygame.key.get_pressed()[K_z]:
            y = y + 20

    ret_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))
    ret_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 40, 50))

    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos += 1
        barulho_colisao.play()

    tela.blit(texto_formatado, (10, 10))

    pygame.display.update()
