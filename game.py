#Icaro Aurich
import random, pygame, datetime, os, sys
from pygame.locals import *
from sys import exit

#roteiro
'''
fazer uma tela que apresente:
tela inicial ()
    O nome do jogo;
    Botão de Ranking > ranking()
    Vai para outra tela que mostra o ranking, com um botão para voltar.
 
    Botão de Sair > Sai do jogo.
 
    Botão de Start;
    pre jogo() 
 
pre jogo ()
    Irá para outra tela perguntando o número de jogadores, e um botão de voltar
    Após ter o número de jogadores, ir para outra tela (pre jogo 2())
pre jogo 2()
    Perguntar o nome dos jogadores e as imagens para o jogador escolher;
    Um botão de confirmar e voltar
    Após a confirmação dos nomes,  (ordem_jogadores())
ordem jogadores()
    tela que mostre a ordem dos jogadores, botão de avançar (chama jogo()), sem voltar;
 jogo()
    Resolução aumenta; blit nas paradas
    jogo roda
    fim do jogo > fim()
fim()
    Apresenta a tela com as posições e dinheiro de todos os jogadores
    botão para voltar para tela inicial (tela inicial())
'''

#defs
def tela_inicial():
    #mixer.music.play()
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if jogar.collidepoint(ev.pos):
                    perguntar_n_jogadores()
                    #mixer.music.play()
                if ranking.collidepoint(ev.pos):tela_ranking()
                if largura // 100 * 10 <= mouse[0] <= largura // 100 * 14 and altura // 100 * 60 <= mouse[1] <= altura // 100 * 62:pygame.quit() #sair
        mouse = pygame.mouse.get_pos()
        tela_1 = pygame.display.set_mode((largura-(px*2), altura-(py*2)))
        pygame.display.set_caption("Tela 1")

        # textos
        texto_nome_jogo = font_nome_game.render('JOGO TOP', True,preto,branco)
        texto_botao_2 = font_32.render('Ranking', True, preto)
        texto_botao_3 = font_32.render('SAIR', True, preto,branco)

        jogar = pygame.Rect((largura // 100) * 10, (altura // 100) * 40, 130, 36)
        ranking = pygame.Rect((largura // 100) * 10, (altura // 100) * 50, 130, 36)
        text_surface1 = font_32.render("JOGAR", True, (0, 0, 0))

        #blit
        tela_1.blit(wallpaper_r, (0,0))
        tela_1.blit(texto_nome_jogo, ((largura // 100) * 40, altura // 9))
        pygame.draw.rect(tela_1, branco, ranking)
        tela_1.blit(texto_botao_2, ((largura // 100) * 10, (altura // 100) * 50)) #ranking
        tela_1.blit(texto_botao_3, ((largura // 100) * 10, (altura // 100) * 60)) #sair

        pygame.draw.rect(tela_1, branco, jogar)

        tela_1.blit(text_surface1, (jogar.x + 5, jogar.y + 5))
        pygame.display.update()
def perguntar_n_jogadores():
    tela_4_b = True
    active = False
    fail = False
    mensagem_fail = "Conteúdo inválido, favor informar um número entre 2 e 4!!"
    conteudo = ['']
    while tela_4_b is True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT: pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if input_n_jogadores.collidepoint(ev.pos):active = True
                else:active = False
                if box_apagar.collidepoint(ev.pos):conteudo=['']
                if confirmar.collidepoint(ev.pos):
                    if conteudo[0] == "2":
                        fail = False
                        pre_jogo(2)
                        tela_4_b = False
                    elif conteudo[0] == "3":
                        fail = False
                        pre_jogo(3)
                        tela_4_b = False
                    elif conteudo[0] == "4":
                        fail = False
                        pre_jogo(4)
                        tela_4_b = False
                    else:fail = True
                if largura // 100 * 10 <= mouse[0] <= largura // 100 * 14 and altura // 100 * 60 <= mouse[1] <= altura // 100 * 62: tela_4_b = False  # sair
            if active:
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_BACKSPACE:conteudo[0] = conteudo[0][:-1]
                    else:conteudo[0] += ev.unicode


        mouse = pygame.mouse.get_pos()
        tela_4 = pygame.display.set_mode((largura - (px * 2), altura - (py * 2)))
        pygame.display.set_caption("Tela 4")

        # textos
        texto_nome_jogo = font_nome_game.render('JOGO TOP', True, preto, branco)
        texto_botao_3 = font_32.render('Voltar', True, preto, branco)
        texto_pergunta = font_32.render('Número de jogadores, 2 a 4', True, preto, branco)

        confirmar = pygame.Rect((largura // 100) * 10, (altura // 100) * 50, 180, 36)
        text_jogar = font_32.render("Confirmar", True, (0, 0, 0))

        #input

        input_n_jogadores = pygame.Rect(200, 350, 152, 36)
        box_apagar = pygame.Rect(370, 350, 36, 36)
        if len(conteudo[0]) > 1: conteudo[0] = conteudo[0][:-1]
        text_surface1 = font_32.render(conteudo[0], True, (0, 0, 0))
        # blit
        tela_4.blit(wallpaper_r, (0, 0))
        tela_4.blit(texto_nome_jogo, ((largura // 100) * 40, altura // 9))
        tela_4.blit(texto_botao_3, ((largura // 100) * 10, (altura // 100) * 60))  # sair
        tela_4.blit(texto_pergunta, ((largura // 100) * 10, (altura // 100) * 30))  # sair
        pygame.draw.rect(tela_4, branco, input_n_jogadores)
        pygame.draw.rect(tela_4, branco, box_apagar)
        tela_4.blit(text_surface1, (input_n_jogadores.x + 5, input_n_jogadores.y + 5))

        pygame.draw.rect(tela_4, branco, confirmar)
        tela_4.blit(text_jogar, (confirmar.x + 5, confirmar.y + 5))

        if fail:
            mensagem_fail_r = font_32.render(mensagem_fail, True, (0, 0, 0))
            fail_box = pygame.Rect((largura // 100) * 10, (altura // 100) * 19, 930, 36)
            pygame.draw.rect(tela_4, branco, fail_box)
            tela_4.blit(mensagem_fail_r, (fail_box.x + 5, fail_box.x + 5))

        pygame.display.update()
def pre_jogo(x):
    tela_2_b = True
    active = False
    active2 = False
    active3 = False
    active4 = False

    nome_dos_jogadores = ['','','','']

    input_nome_1 = pygame.Rect(200, 350, 152, 36)
    input_nome_2 = pygame.Rect(200, 400, 152, 36)
    input_nome_3 = pygame.Rect(200, 450, 152, 36)
    input_nome_4 = pygame.Rect(200, 500, 152, 36)
    confirmar = pygame.Rect(200, 600, 190, 36)
    voltar = pygame.Rect(200, 700, 135, 36)

    while tela_2_b is True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if input_nome_1.collidepoint(ev.pos):active = True
                else:active = False
                if input_nome_2.collidepoint(ev.pos):active2 = True
                else:active2 = False
                if input_nome_3.collidepoint(ev.pos):active3 = True
                else:active3 = False
                if input_nome_4.collidepoint(ev.pos):active4 = True
                else:active4 = False
                if confirmar.collidepoint(ev.pos):
                    escolher_personagem(x,nome_dos_jogadores)
                    tela_2_b = False
                if voltar.collidepoint(ev.pos):tela_2_b = False

            if active:
                if ev.type == pygame.KEYDOWN:
                    #pygame.display.flip()
                    if ev.key == pygame.K_BACKSPACE:nome_dos_jogadores[0] = nome_dos_jogadores[0][:-1]
                    else:nome_dos_jogadores[0] += ev.unicode
            if active2:
                if ev.type == pygame.KEYDOWN:
                    #pygame.display.flip()
                    if ev.key == pygame.K_BACKSPACE:nome_dos_jogadores[1] = nome_dos_jogadores[1][:-1]
                    else:nome_dos_jogadores[1] += ev.unicode
            if active3:
                if ev.type == pygame.KEYDOWN:
                    #pygame.display.flip()
                    if ev.key == pygame.K_BACKSPACE:nome_dos_jogadores[2] = nome_dos_jogadores[2][:-1]
                    else:nome_dos_jogadores[2] += ev.unicode
            if active4:
                if ev.type == pygame.KEYDOWN:
                    #pygame.display.flip()
                    if ev.key == pygame.K_BACKSPACE:nome_dos_jogadores[3] = nome_dos_jogadores[3][:-1]
                    else:nome_dos_jogadores[3] += ev.unicode

        mouse = pygame.mouse.get_pos()
        tela_2 = pygame.display.set_mode((largura - (px * 2), altura - (py * 2)))
        pygame.display.set_caption("Tela 2")
        jogador = 1
        for perguntar in range(x):
            perguntar_nome_jogador = "Nome do jogadores"
            # textos
            texto_nome_jogo = font_nome_game.render('JOGO TOP', True, preto, branco)
            texto_qt_jog = font_32.render(perguntar_nome_jogador, True, preto, branco)
            #texto_botao_voltar = font_32.render('voltar', True, preto, branco)

            #blit
            tela_2.blit(wallpaper_r, (0, 0))
            tela_2.blit(texto_nome_jogo, ((largura // 100) * 40, altura // 9))
            #tela_2.blit(texto_botao_voltar, ((largura // 100) * 10, (altura // 100) * 10))  # voltar
            tela_2.blit(texto_qt_jog, ((largura // 100) * 10, (altura // 100) * 30))  #texto
            n=1
            for drawrect in range(x):
                local = eval("input_nome_"+str(n))
                pygame.draw.rect(tela_2,branco, local)
                n+=1
            pygame.draw.rect(tela_2,branco, confirmar)
            pygame.draw.rect(tela_2,branco, voltar)
            if len(nome_dos_jogadores[0]) > 8: nome_dos_jogadores[0] = nome_dos_jogadores[0][:-1]
            if len(nome_dos_jogadores[1]) > 8: nome_dos_jogadores[1] = nome_dos_jogadores[1][:-1]
            if len(nome_dos_jogadores[2]) > 8: nome_dos_jogadores[2] = nome_dos_jogadores[2][:-1]
            if len(nome_dos_jogadores[3]) > 8: nome_dos_jogadores[3] = nome_dos_jogadores[3][:-1]
            text_surface1 = font_32.render(nome_dos_jogadores[0], True, (0, 0, 0))
            text_surface2 = font_32.render(nome_dos_jogadores[1], True, (0, 0, 0))
            text_surface3 = font_32.render(nome_dos_jogadores[2], True, (0, 0, 0))
            text_surface4 = font_32.render(nome_dos_jogadores[3], True, (0, 0, 0))
            confirmar_t = font_32.render("Confirmar !", True, (0, 0, 0))
            voltar_t = font_32.render("VOLTAR", True, (0, 0, 0))
            tela_2.blit(text_surface1, (input_nome_1.x + 5, input_nome_1.y + 5))
            tela_2.blit(text_surface2, (input_nome_2.x + 5, input_nome_2.y + 5))
            tela_2.blit(text_surface3, (input_nome_3.x + 5, input_nome_3.y + 5))
            tela_2.blit(text_surface4, (input_nome_4.x + 5, input_nome_4.y + 5))
            tela_2.blit(confirmar_t, (confirmar.x + 5, confirmar.y + 5))
            tela_2.blit(voltar_t, (voltar.x + 5, voltar.y + 5))

            pygame.display.update()
def escolher_personagem(x,nome_dos_jogadores):
    tela_3_b = True
    #bol do player 1
    p1_1_b = False
    p1_2_b = False
    p1_3_b = False
    p1_4_b = False
    p1_5_b = False
    p1_6_b = False
    # bol do player 2
    p2_1_b = False
    p2_2_b = False
    p2_3_b = False
    p2_4_b = False
    p2_5_b = False
    p2_6_b = False
    # bol do player 3
    p3_1_b = False
    p3_2_b = False
    p3_3_b = False
    p3_4_b = False
    p3_5_b = False
    p3_6_b = False
    # bol do player 4
    p4_1_b = False
    p4_2_b = False
    p4_3_b = False
    p4_4_b = False
    p4_5_b = False
    p4_6_b = False
    jogadores_2 = False
    jogadores_3 = False
    jogadores_4 = False
    dinheiro_players = [1000,1000,1000,1000]
    personagens = [0,0,0,0]
    while tela_3_b is True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if voltar.collidepoint(ev.pos): tela_3_b=False
                if confirmar.collidepoint(ev.pos):
                    jogo(x,nome_dos_jogadores,dinheiro_players,personagens)
                    tela_3_b = False

                if p1_1.collidepoint(ev.pos):
                    p1_1_b = True
                    personagens[0] = 1
                    p1_2_b = False
                    p1_3_b = False
                    p1_4_b = False
                    p1_5_b = False
                    p1_6_b = False
                if p1_2.collidepoint(ev.pos):
                    p1_1_b = False
                    p1_2_b = True
                    personagens[0] = 2
                    p1_3_b = False
                    p1_4_b = False
                    p1_5_b = False
                    p1_6_b = False
                if p1_3.collidepoint(ev.pos):
                    p1_1_b = False
                    p1_2_b = False
                    p1_3_b = True
                    personagens[0] = 3
                    p1_4_b = False
                    p1_5_b = False
                    p1_6_b = False
                if p1_4.collidepoint(ev.pos):
                    p1_1_b = False
                    p1_2_b = False
                    p1_3_b = False
                    p1_4_b = True
                    personagens[0] = 4
                    p1_5_b = False
                    p1_6_b = False
                if p1_5.collidepoint(ev.pos):
                    p1_1_b = False
                    p1_2_b = False
                    p1_3_b = False
                    p1_4_b = False
                    p1_5_b = True
                    personagens[0] = 5
                    p1_6_b = False
                if p1_6.collidepoint(ev.pos):
                    p1_1_b = False
                    p1_2_b = False
                    p1_3_b = False
                    p1_4_b = False
                    p1_5_b = False
                    p1_6_b = True
                    personagens[0] = 6

                if p2_1.collidepoint(ev.pos):
                    p2_1_b = True
                    personagens[1] = 1
                    p2_2_b = False
                    p2_3_b = False
                    p2_4_b = False
                    p2_5_b = False
                    p2_6_b = False
                if p2_2.collidepoint(ev.pos):
                    p2_1_b = False
                    p2_2_b = True
                    personagens[1] = 2
                    p2_3_b = False
                    p2_4_b = False
                    p2_5_b = False
                    p2_6_b = False
                if p2_3.collidepoint(ev.pos):
                    p2_1_b = False
                    p2_2_b = False
                    p2_3_b = True
                    personagens[1] = 3
                    p2_4_b = False
                    p2_5_b = False
                    p2_6_b = False
                if p2_4.collidepoint(ev.pos):
                    p2_1_b = False
                    p2_2_b = False
                    p2_3_b = False
                    p2_4_b = True
                    personagens[1] = 4
                    p2_5_b = False
                    p2_6_b = False
                if p2_5.collidepoint(ev.pos):
                    p2_1_b = False
                    p2_2_b = False
                    p2_3_b = False
                    p2_4_b = False
                    p2_5_b = True
                    personagens[1] = 5
                    p2_6_b = False
                if p2_6.collidepoint(ev.pos):
                    p2_1_b = False
                    p2_2_b = False
                    p2_3_b = False
                    p2_4_b = False
                    p2_5_b = False
                    p2_6_b = True
                    personagens[1] = 6

                if p3_1.collidepoint(ev.pos):
                    p3_1_b = True
                    personagens[2] = 1
                    p3_2_b = False
                    p3_3_b = False
                    p3_4_b = False
                    p3_5_b = False
                    p3_6_b = False
                if p3_2.collidepoint(ev.pos):
                    p3_1_b = False
                    p3_2_b = True
                    personagens[2] = 2
                    p3_3_b = False
                    p3_4_b = False
                    p3_5_b = False
                    p3_6_b = False
                if p3_3.collidepoint(ev.pos):
                    p3_1_b = False
                    p3_2_b = False
                    p3_3_b = True
                    personagens[2] = 3
                    p3_4_b = False
                    p3_5_b = False
                    p3_6_b = False
                if p3_4.collidepoint(ev.pos):
                    p3_1_b = False
                    p3_2_b = False
                    p3_3_b = False
                    p3_4_b = True
                    personagens[2] = 4
                    p3_5_b = False
                    p3_6_b = False
                if p3_5.collidepoint(ev.pos):
                    p3_1_b = False
                    p3_2_b = False
                    p3_3_b = False
                    p3_4_b = False
                    p3_5_b = True
                    personagens[2] = 5
                    p3_6_b = False
                if p3_6.collidepoint(ev.pos):
                    p3_1_b = False
                    p3_2_b = False
                    p3_3_b = False
                    p3_4_b = False
                    p3_5_b = False
                    p3_6_b = True
                    personagens[2] = 6

                if p4_1.collidepoint(ev.pos):
                    p4_1_b = True
                    personagens[3] = 1
                    p4_2_b = False
                    p4_3_b = False
                    p4_4_b = False
                    p4_5_b = False
                    p4_6_b = False
                if p4_2.collidepoint(ev.pos):
                    p4_1_b = False
                    p4_2_b = True
                    personagens[3] = 2
                    p4_3_b = False
                    p4_4_b = False
                    p4_5_b = False
                    p4_6_b = False
                if p4_3.collidepoint(ev.pos):
                    p4_1_b = False
                    p4_2_b = False
                    p4_3_b = True
                    personagens[3] = 3
                    p4_4_b = False
                    p4_5_b = False
                    p4_6_b = False
                if p4_4.collidepoint(ev.pos):
                    p4_1_b = False
                    p4_2_b = False
                    p4_3_b = False
                    p4_4_b = True
                    personagens[3] = 4
                    p4_5_b = False
                    p4_6_b = False
                if p4_5.collidepoint(ev.pos):
                    p4_1_b = False
                    p4_2_b = False
                    p4_3_b = False
                    p4_4_b = False
                    p4_5_b = True
                    personagens[3] = 5
                    p4_6_b = False
                if p4_6.collidepoint(ev.pos):
                    p4_1_b = False
                    p4_2_b = False
                    p4_3_b = False
                    p4_4_b = False
                    p4_5_b = False
                    p4_6_b = True
                    personagens[3] = 6


        mouse = pygame.mouse.get_pos()
        #setando as paradas
        tela_3 = pygame.display.set_mode((largura - (px * 2), altura - (py * 2)))
        pygame.display.set_caption("Tela 3")

        confirmar = pygame.Rect(200, 700, 220, 36)
        voltar = pygame.Rect(200, 750, 135, 36)
        texto_img_1_box = pygame.Rect(80, 50, 930, 36)
        texto_img_2_box = pygame.Rect(80, 200, 930, 36)
        texto_img_3_box = pygame.Rect(80, 350, 930, 36)
        texto_img_4_box = pygame.Rect(80, 500, 930, 36)
        p1_1 = pygame.Rect(100, 100, 80, 100)
        p1_2 = pygame.Rect(200, 100, 80, 100)
        p1_3 = pygame.Rect(300, 100, 80, 100)
        p1_4 = pygame.Rect(400, 100, 80, 100)
        p1_5 = pygame.Rect(500, 100, 80, 100)
        p1_6 = pygame.Rect(600, 100, 80, 100)

        p2_1 = pygame.Rect(100, 250, 80, 100)
        p2_2 = pygame.Rect(200, 250, 80, 100)
        p2_3 = pygame.Rect(300, 250, 80, 100)
        p2_4 = pygame.Rect(400, 250, 80, 100)
        p2_5 = pygame.Rect(500, 250, 80, 100)
        p2_6 = pygame.Rect(600, 250, 80, 100)

        p3_1 = pygame.Rect(100, 400, 80, 100)
        p3_2 = pygame.Rect(200, 400, 80, 100)
        p3_3 = pygame.Rect(300, 400, 80, 100)
        p3_4 = pygame.Rect(400, 400, 80, 100)
        p3_5 = pygame.Rect(500, 400, 80, 100)
        p3_6 = pygame.Rect(600, 400, 80, 100)

        p4_1 = pygame.Rect(100, 550, 80, 100)
        p4_2 = pygame.Rect(200, 550, 80, 100)
        p4_3 = pygame.Rect(300, 550, 80, 100)
        p4_4 = pygame.Rect(400, 550, 80, 100)
        p4_5 = pygame.Rect(500, 550, 80, 100)
        p4_6 = pygame.Rect(600, 550, 80, 100)

        texto_botao_voltar = font_32.render('VOLTAR', True, preto)
        texto_botao_confirmar = font_32.render('CONFIRMAR', True, preto)
        player_1_text = nome_dos_jogadores[0] + ", escolha seu personagem!"
        player_2_text = nome_dos_jogadores[1] + ", escolha seu personagem!"
        player_3_text = nome_dos_jogadores[2] + ", escolha seu personagem!"
        player_4_text = nome_dos_jogadores[3] + ", escolha seu personagem!"
        texto_img_1 = font_32.render(player_1_text, True, preto)
        texto_img_2 = font_32.render(player_2_text, True, preto)
        texto_img_3 = font_32.render(player_3_text, True, preto)
        texto_img_4 = font_32.render(player_4_text, True, preto)
        #blit
        tela_3.blit(wallpaper_r, (0, 0))
        n=1

        if x >= 2:jogadores_2 = True
        if x >= 3:jogadores_3 = True
        if x >= 4:jogadores_4 = True
        if jogadores_2:
            for print_rect_player_1 in range(6):
                variavel_boleana = eval("p1_"+str(n)+"_b")
                variavel_boleana_p = eval("p1_" + str(n))
                if variavel_boleana == True:pygame.draw.rect(tela_3, verde, variavel_boleana_p)
                else:pygame.draw.rect(tela_3, branco, variavel_boleana_p)
                n+=1
                if n==7:n=1
            n=1
            p=100
            for player_1 in range(6):
                imagem = eval("imagem_" + str(n) + "_r")
                tela_3.blit(imagem, (p, 100))
                n+=1
                p+=100
            n=1
            p=100
            tela_3.blit(texto_img_1, (texto_img_1_box.x + 5, texto_img_1_box.y + 5))
            for print_rect_player_2 in range(6):
                variavel_boleana = eval("p2_"+str(n)+"_b")
                variavel_boleana_p = eval("p2_" + str(n))
                if variavel_boleana == True:pygame.draw.rect(tela_3, verde, variavel_boleana_p)
                else:pygame.draw.rect(tela_3, branco, variavel_boleana_p)
                n+=1
                if n==7:n=1
            n=1
            p=100
            for player_2 in range(6):
                imagem = eval("imagem_" + str(n) + "_r")
                tela_3.blit(imagem, (p, 250))
                n+=1
                p+=100
            tela_3.blit(texto_img_2, (texto_img_2_box.x + 5, texto_img_2_box.y + 5))
        n = 1
        if jogadores_3:
            for print_rect_player_3 in range(6):
                variavel_boleana = eval("p3_" + str(n) + "_b")
                variavel_boleana_p = eval("p3_" + str(n))
                if variavel_boleana == True:
                    pygame.draw.rect(tela_3, verde, variavel_boleana_p)
                else:
                    pygame.draw.rect(tela_3, branco, variavel_boleana_p)
                n += 1
                if n == 7: n = 1
            n = 1
            p = 100
            for player_3 in range(6):
                imagem = eval("imagem_" + str(n) + "_r")
                tela_3.blit(imagem, (p, 400))
                n += 1
                p += 100
            tela_3.blit(texto_img_3, (texto_img_3_box.x + 5, texto_img_3_box.y + 5))
        n = 1
        if jogadores_4:
            for print_rect_player_4 in range(6):
                variavel_boleana = eval("p4_" + str(n) + "_b")
                variavel_boleana_p = eval("p4_" + str(n))
                if variavel_boleana == True:
                    pygame.draw.rect(tela_3, verde, variavel_boleana_p)
                else:
                    pygame.draw.rect(tela_3, branco, variavel_boleana_p)
                n += 1
                if n == 7: n = 1
            n = 1
            p = 100
            for player_4 in range(6):
                imagem = eval("imagem_" + str(n) + "_r")
                tela_3.blit(imagem, (p, 550))
                n += 1
                p += 100
            tela_3.blit(texto_img_4, (texto_img_4_box.x + 5, texto_img_4_box.y + 5))

        pygame.draw.rect(tela_3, branco, voltar)
        pygame.draw.rect(tela_3, branco, confirmar)
        tela_3.blit(texto_botao_voltar, (voltar.x + 5, voltar.y + 5))
        tela_3.blit(texto_botao_confirmar, (confirmar.x + 5, confirmar.y + 5))

        pygame.display.update()
def jogo(x,nome_dos_jogadores,dinheiro_players,personagens):
    def rodar_roleta():
        contador = 1
        for a in range(2):
            roleta = eval(str("roleta_" + str(contador)))
            tela_5.blit(roleta, (1390, 480))
            pygame.display.update()
            pygame.time.delay(50)
            contador += 1
            if contador == 7: contador = 1
    def numero_random2():
        numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        return random.choice(numeros)
    def jogar_o_dado():
        return numero_random()
    def numero_random():
        numeros = [1, 2, 3, 4, 5]
        return random.choice(numeros)
    def blit():
        peca_jogador_1 = eval("imagem_"+str(personagens[0])+"_r2")
        peca_jogador_2 = eval("imagem_"+str(personagens[1])+"_r2")
        peca_jogador_3 = eval("imagem_"+str(personagens[2])+"_r2")
        peca_jogador_4 = eval("imagem_"+str(personagens[3])+"_r2")
        pp1 = posicao_dos_jogadores[0]
        pp2 = posicao_dos_jogadores[1]
        pp3 = posicao_dos_jogadores[2]
        pp4 = posicao_dos_jogadores[3]
        tela_5.blit(peca_jogador_1, (posicoes[pp1][0] - 20, posicoes[pp1][1] - 20))
        tela_5.blit(peca_jogador_2, (posicoes[pp2][0] + 20, posicoes[pp2][1] + 20))
        tela_5.blit(peca_jogador_3, (posicoes[pp3][0] + 20, posicoes[pp3][1] - 20))
        tela_5.blit(peca_jogador_4, (posicoes[pp4][0] - 20, posicoes[pp4][1] + 20))
        textpnt = (1530, 20)
        textpj1 = (1385, 50)
        textpj1p = (1390, 90)
        textpj1d = (1390, 110)
        textpj2 = (1385, 140)
        textpj2p = (1390, 180)
        textpj2d = (1390, 200)
        textpj3 = (1385, 230)
        textpj3p = (1390, 270)
        textpj3d = (1390, 290)
        textpj4 = (1385, 320)
        textpj4p = (1390, 360)
        textpj4d = (1390, 380)
        textrodada1p = (1380, 420)  # vez de
        textrodada2p = (1380, 440)  # ocorrido
        textrodada3p = (1380, 460)  # perca ou ganhe

        # textos
        textj1p = font_16.render("Posição: " + str(posicao_dos_jogadores[0] + 1), True, azul, branco)
        textj1d = font_16.render("Dinheiro: " + str(dinheiro_players[0]), True, azul, branco)
        textj2p = font_16.render("Posição: " + str(posicao_dos_jogadores[1] + 1), True, azul, branco)
        textj2d = font_16.render("Dinheiro: " + str(dinheiro_players[1]), True, azul, branco)
        textj3p = font_16.render("Posição: " + str(posicao_dos_jogadores[2] + 1), True, azul, branco)
        textj3d = font_16.render("Dinheiro: " + str(dinheiro_players[2]), True, azul, branco)
        textj4p = font_16.render("Posição: " + str(posicao_dos_jogadores[3] + 1), True, azul, branco)
        textj4d = font_16.render("Dinheiro: " + str(dinheiro_players[3]), True, azul, branco)
        textrodada1 = font_16.render("Vez de: " + str(jogador_atual), True, azul, branco)  # vez de, leia
        textrodada2 = font_16.render(ocorrido, True, azul, branco)  # ocorrido
        textrodada3 = font_16.render(ocorrido2, True, azul, branco)  # perca ou ganhe

        # blit
        tela_5.blit(txt_pontuacao, textpnt)
        tela_5.blit(txtj1, textpj1)
        tela_5.blit(textj1p, textpj1p)
        tela_5.blit(textj1d, textpj1d)
        tela_5.blit(txtj2, textpj2)
        tela_5.blit(textj2p, textpj2p)
        tela_5.blit(textj2d, textpj2d)
        tela_5.blit(txtj3, textpj3)
        tela_5.blit(textj3p, textpj3p)
        tela_5.blit(textj3d, textpj3d)
        tela_5.blit(txtj4, textpj4)
        tela_5.blit(textj4p, textpj4p)
        tela_5.blit(textj4d, textpj4d)
        tela_5.blit(textrodada1, textrodada1p)
        tela_5.blit(textrodada2, textrodada2p)
        tela_5.blit(textrodada3, textrodada3p)
        pygame.display.update()
        pygame.time.delay(50)
    def conselho(jogador, lista_boa, lista_ruim, rodado):
        if jogador in lista_boa:
            dinheiro_atual = supresa_boa(rodado)
            return dinheiro_atual
        elif jogador in lista_ruim:
            dinheiro_atual = supresa_ruim(rodado)
            return dinheiro_atual
        else:
            ocorrido = "Nada aconteceu"
            return ocorrido
    def conselho2(jogador, lista_boa, lista_ruim, rodado):
        if jogador in lista_boa:
            dinheiro_atual = supresa_boa2(rodado)
            return dinheiro_atual
        elif jogador in lista_ruim:
            dinheiro_atual = supresa_ruim2(rodado)
            return dinheiro_atual
        else:
            return 0
    def conselho3(jogador, lista_boa, lista_ruim, rodado):
        if jogador in lista_boa:
            dinheiro_atual = supresa_boa3(rodado)
            return dinheiro_atual
        elif jogador in lista_ruim:
            dinheiro_atual = supresa_ruim3(rodado)
            return dinheiro_atual
        else:
            ocorrido = ""
            return ocorrido
    def supresa_ruim(rodado):
        if rodado == 1:
            dinheiro_atual = "Acabou o gás"
            return dinheiro_atual
        if rodado == 2:
            dinheiro_atual = "Motoboy quebrou o retrovisor"
            return dinheiro_atual
        if rodado == 3:
            dinheiro_atual = "Queimou a resistência do chuveiro"
            return dinheiro_atual
        if rodado == 4:
            dinheiro_atual = "Acabou a gasolina"
            return dinheiro_atual
        if rodado == 5:
            dinheiro_atual = "Seu filho gastou 500 no FORTINE"
            return dinheiro_atual
        if rodado == 6:
            dinheiro_atual = "Você vai ser pai"
            return dinheiro_atual
        if rodado == 7:
            dinheiro_atual = "Você foi multado"
            return dinheiro_atual
        if rodado == 8:
            dinheiro_atual = "Pagar o agiota"
            return dinheiro_atual
        if rodado == 9:
            dinheiro_atual = "Perdeu no jogo do bicho"
            return dinheiro_atual
        if rodado == 10:
            dinheiro_atual = "AZARAÇÃO CRITICA - Você é feio, pagar plástica"
            return dinheiro_atual
    def supresa_ruim3(rodado):
        if rodado == 1:
            dinheiro_atual = "Dinheiro do jogador caiu 60 reais"
            return dinheiro_atual
        if rodado == 2:
            dinheiro_atual = "Dinheiro do jogador caiu 100 reais para pagar o retrovisor"
            return dinheiro_atual
        if rodado == 3:
            dinheiro_atual = "Dinheiro do jogador caiu 30 reais"
            return dinheiro_atual
        if rodado == 4:
            dinheiro_atual = "Dinheiro do jogador caiu 100 reais"
            return dinheiro_atual
        if rodado == 5:
            dinheiro_atual = "Dinheiro do jogador caiu 500 reais"
            return dinheiro_atual
        if rodado == 6:
            dinheiro_atual = "Dinheiro do jogador caiu 1000 reais"
            return dinheiro_atual
        if rodado == 7:
            dinheiro_atual = "Dinheiro do jogador caiu 300 reais"
            return dinheiro_atual
        if rodado == 8:
            dinheiro_atual = "Dinheiro do jogador caiu 800 reais"
            return dinheiro_atual
        if rodado == 9:
            dinheiro_atual = "Dinheiro do jogador caiu 200 reais"
            return dinheiro_atual
        if rodado == 10:
            dinheiro_atual = "Dinheiro do jogador caiu 2000 reais"
            return dinheiro_atual
    def supresa_ruim2(rodado):
        if rodado == 1:
            dinheiro_atual = -60
            return dinheiro_atual
        if rodado == 2:
            dinheiro_atual = -100
            return dinheiro_atual
        if rodado == 3:
            dinheiro_atual = -30
            return dinheiro_atual
        if rodado == 4:
            dinheiro_atual = -100
            return dinheiro_atual
        if rodado == 5:
            dinheiro_atual = -500
            return dinheiro_atual
        if rodado == 6:
            dinheiro_atual = -1000
            return dinheiro_atual
        if rodado == 7:
            dinheiro_atual = -300
            return dinheiro_atual
        if rodado == 8:
            dinheiro_atual = -800
            return dinheiro_atual
        if rodado == 9:
            dinheiro_atual = -200
            return dinheiro_atual
        if rodado == 10:
            dinheiro_atual = -2000
            return dinheiro_atual
    def supresa_boa(rodado):
        if rodado == 1:
            ocorrido = "Achou 50 reais na rua"
            return ocorrido
        if rodado == 2:
            ocorrido = "Você achou um anel na rua"
            return ocorrido
        if rodado == 3:
            ocorrido = "Você ajudou a idosa a atravessar a rua"
            return ocorrido
        if rodado == 4:
            ocorrido = "Você processou o posto e ganhou"
            return ocorrido
        if rodado == 5:
            ocorrido = "Você conseguiu reembolso do FORTNITE"
            return ocorrido
        if rodado == 6:
            ocorrido = "Você não vai ser pai"
            return ocorrido
        if rodado == 7:
            ocorrido = "Você separou da morena, menos um gasto nas sua vida"
            return ocorrido
        if rodado == 8:
            ocorrido = "Agiota tem Alzheimer"
            return ocorrido
        if rodado == 9:
            ocorrido = "Ganhou no jogo do bicho"
            return ocorrido
        if rodado == 10:
            ocorrido = "SORTE CRITICA - Você ganhou na loteria"
            return ocorrido
    def supresa_boa3(rodado):
        if rodado == 1:
            ocorrido = "Dinheiro do jogador subiu 50 reais"
            return ocorrido
        if rodado == 2:
            ocorrido = "Dinheiro do jogador subiu 100 reais"
            return ocorrido
        if rodado == 3:
            ocorrido = "Dinheiro do jogador subiu 30 reais"
            return ocorrido
        if rodado == 4:
            ocorrido = "Dinheiro do jogador subiu 100 reais"
            return ocorrido
        if rodado == 5:
            ocorrido = "Dinheiro do jogador subiu 500 reais"
            return ocorrido
        if rodado == 6:
            ocorrido = "Dinheiro do jogador não subiu nem desceu"
            return ocorrido
        if rodado == 7:
            ocorrido = "Dinheiro do jogador subiu 300 reais"
            return ocorrido
        if rodado == 8:
            ocorrido = "Dinheiro do jogador subiu 800 reais"
            return ocorrido
        if rodado == 9:
            ocorrido = "Dinheiro do jogador subiu 200 reais"
            return ocorrido
        if rodado == 10:
            ocorrido = "Dinheiro do jogador subiu 1000 reais"
            return ocorrido
    def supresa_boa2(rodado):
        if rodado == 1:
            dinheiro_atual = 50
            return dinheiro_atual
        if rodado == 2:
            dinheiro_atual = 100
            return dinheiro_atual
        if rodado == 3:
            dinheiro_atual = 30
            return dinheiro_atual
        if rodado == 4:
            dinheiro_atual = 100
            return dinheiro_atual
        if rodado == 5:
            dinheiro_atual = 500
            return dinheiro_atual
        if rodado == 6:
            dinheiro_atual = 0
            return dinheiro_atual
        if rodado == 7:
            dinheiro_atual = 300
            return dinheiro_atual
        if rodado == 8:
            dinheiro_atual = 800
            return dinheiro_atual
        if rodado == 9:
            dinheiro_atual = 200
            return dinheiro_atual
        if rodado == 10:
            dinheiro_atual = 1000
            return dinheiro_atual
    posicao_dos_jogadores = [0,0,0,0]
    jogo_aberto = True
    jogo_aberto_final = True
    while jogo_aberto_final is True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
        tela_5 = pygame.display.set_mode((largura - (px * 2), altura - (py * 2)))
        pygame.display.set_caption("Tela 5")

        #textos
        txt_pontuacao = font_32.render('PONTUAÇÃO', True, azul, branco)
        txtj1 = font_16.render(nome_dos_jogadores[0], True, azul, branco)
        txtj2 = font_16.render(nome_dos_jogadores[1], True, azul, branco)
        txtj3 = font_16.render(nome_dos_jogadores[2], True, azul, branco)
        txtj4 = font_16.render(nome_dos_jogadores[3], True, azul, branco)


        while jogo_aberto is True:
            contador = 0
            for a in range(x):
                tela_5.blit(wallpaper_r, (0, 0))
                tela_5.blit(fundo_score, (1367, 10))
                tela_5.blit(tabuleiro, (0, 0))
                ocorrido = ""
                ocorrido2 = ""
                rodado = numero_random2()
                dinheiro_atual = 0
                jogador = 0
                jogador_atual = eval("nome_dos_jogadores[" + str(contador)+"]")
                jogador = jogar_o_dado()

                blit()
                rodar_roleta()

                roleta = eval(str("roleta_" + str(jogador)))
                tela_5.blit(roleta, (1390, 480))
                blit()
                ocorrido = conselho(eval("posicao_dos_jogadores[" + str(contador)+"]") + jogador, lista_boa, lista_ruim, rodado)
                ocorrido2 = conselho3(eval("posicao_dos_jogadores[" + str(contador)+"]") + jogador, lista_boa, lista_ruim, rodado)
                dinheiro_atual = conselho2(eval("posicao_dos_jogadores[" + str(contador)+"]") + jogador, lista_boa, lista_ruim, rodado)
                blit()

                if contador == 0:
                    posicao_dos_jogadores[0] = posicao_dos_jogadores[0] + jogador
                    dinheiro_players[0] = dinheiro_players[0] + (dinheiro_atual)
                elif contador == 1:
                    posicao_dos_jogadores[1] = posicao_dos_jogadores[1] + jogador
                    dinheiro_players[1] = dinheiro_players[1] + (dinheiro_atual)
                elif contador == 2:
                    posicao_dos_jogadores[2] = posicao_dos_jogadores[2] + jogador
                    dinheiro_players[2] = dinheiro_players[2] + (dinheiro_atual)
                elif contador == 3:
                    posicao_dos_jogadores[3] = posicao_dos_jogadores[3] + jogador
                    dinheiro_players[3] = dinheiro_players[3] + (dinheiro_atual)

                if posicao_dos_jogadores[0] >= fim:
                    vencedor = nome_dos_jogadores[0]
                    dinheiro = dinheiro_players[0]
                    imagem_ganhador =  personagens[0]
                    jogo_aberto = False
                    break
                if posicao_dos_jogadores[1] >= fim:
                    vencedor = nome_dos_jogadores[1]
                    dinheiro = dinheiro_players[1]
                    imagem_ganhador = personagens[1]
                    jogo_aberto = False
                    break
                if posicao_dos_jogadores[2] >= fim:
                    vencedor = nome_dos_jogadores[2]
                    dinheiro = dinheiro_players[2]
                    imagem_ganhador = personagens[2]
                    jogo_aberto = False
                    break
                if posicao_dos_jogadores[3] >= fim:
                    vencedor = nome_dos_jogadores[3]
                    dinheiro = dinheiro_players[3]
                    imagem_ganhador = personagens[2]
                    jogo_aberto = False
                    break
                else:
                    contador = contador + 1
                pygame.time.delay(500)

        mixer.music.load('fim_de_jogo.wav')
        mixer.music.play()
        pygame.display.update()
        arquivo = open('ranking.txt', 'a')
        arquivo.write(str(dinheiro) + "," + str(vencedor) + "\n")
        arquivo.close()
        imagem_ganhador = str(imagem_ganhador)
        fim_de_jogo(vencedor,dinheiro,imagem_ganhador)
        jogo_aberto_final = False
def fim_de_jogo(vencedor,dinheiro,imagem_ganhador):
    jogo_final_aberto = True
    while jogo_final_aberto is True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if sair.collidepoint(ev.pos):
                    mixer.music.load('musiquinha_top.wav')
                    jogo_final_aberto = False

        mouse = pygame.mouse.get_pos()
        tela_6 = pygame.display.set_mode((largura - (px * 2), altura - (py * 2)))
        pygame.display.set_caption("Tela 6")

        # textos
        texto_nome_jogo = font_nome_game.render('JOGO TOP', True,preto,branco)
        texto_botao_2 = font_32.render('Voltar ao início', True, preto)
        texto_nome_ganhador = font_32.render(vencedor + " ganhou!!", True, preto)
        texto_dinheiro_ganhador = font_32.render(str("Saldo: " + str(dinheiro)), True, preto)
        imagem_ganhador_final = eval("imagem_" + str(imagem_ganhador) + "_r")
        sair = pygame.Rect((largura // 100) * 10, (altura // 100) * 70, 250, 36)

        #blit
        tela_6.blit(wallpaper_r, (0, 0))
        tela_6.blit(imagem_ganhador_final, (400, 200))
        tela_6.blit(texto_nome_jogo, ((largura // 100) * 40, altura // 9))
        pygame.draw.rect(tela_6, branco, sair)
        tela_6.blit(texto_botao_2, ((largura // 100) * 10, (altura // 100) * 70)) #ranking
        tela_6.blit(texto_nome_ganhador, (100,100)) #ranking
        tela_6.blit(texto_dinheiro_ganhador, (200,200)) #ranking

        pygame.display.update()
def tela_ranking():
    arquivo = open('ranking.txt', 'r')
    text = []
    for line in arquivo:
        text.append(line)
    print(text)
    text.sort()
    text.reverse()
    print(text)
    teste = str(text)
    teste_0 = teste.replace("\\n",'')
    teste_1 = teste_0.replace("]",'')
    teste_2 = teste_1.replace("[",'')
    teste_3 = teste_2.replace("'",'')
    lista = str(teste_3).split(",")
    print(lista)
    lista_nome = []
    lista_saldo = []
    cont1 = 0
    cont2 = 1
    try:
        for top in range(10):
            lista_nome.append(lista[cont1])
            lista_saldo.append(lista[cont2])
            cont1 +=2
            cont2+=2
    except:print("fim da leitura")
    ranking_aberto = True
    while ranking_aberto is True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT: pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if voltar.collidepoint(ev.pos):
                    ranking_aberto = False

        #text = '\n'.join(text)
        mouse = pygame.mouse.get_pos()
        tela_6 = pygame.display.set_mode((largura - (px * 2), altura - (py * 2)))
        pygame.display.set_caption("Tela 6")

        # textos
        texto_nome_jogo = font_nome_game.render('Ranking', True, preto, branco)
        texto_botao_2 = font_32.render('Voltar', True, preto)
        texto_nome_1 = font_32.render(str(lista_nome[0]), True, preto)
        texto_nome_2 = font_32.render(str(lista_saldo[0]), True, preto)
        texto_nome_3 = font_32.render(str(lista_nome[1]), True, preto)
        texto_nome_4 = font_32.render(str(lista_saldo[1]), True, preto)
        texto_nome_5 = font_32.render(str(lista_nome[2]), True, preto)
        texto_nome_6 = font_32.render(str(lista_saldo[2]), True, preto)
        texto_nome_7 = font_32.render(str(lista_nome[3]), True, preto)
        texto_nome_8 = font_32.render(str(lista_saldo[3]), True, preto)
        texto_nome_9 = font_32.render(str(lista_nome[4]), True, preto)
        texto_nome_10 = font_32.render(str(lista_saldo[4]), True, preto)
        texto_nome_11 = font_32.render(str(lista_nome[5]), True, preto)
        texto_nome_12 = font_32.render(str(lista_saldo[5]), True, preto)
        texto_nome_13 = font_32.render(str(lista_nome[6]), True, preto)
        texto_nome_14 = font_32.render(str(lista_saldo[6]), True, preto)
        texto_nome_15 = font_32.render(str(lista_nome[7]), True, preto)
        texto_nome_16 = font_32.render(str(lista_saldo[7]), True, preto)
        texto_nome_17 = font_32.render(str(lista_nome[8]), True, preto)
        texto_nome_18 = font_32.render(str(lista_saldo[8]), True, preto)
        texto_nome_19 = font_32.render(str(lista_nome[9]), True, preto)
        texto_nome_20 = font_32.render(str(lista_saldo[9]), True, preto)
        #texto_nome_ganhador = font_32.render(vencedor + " ganhou!!", True, preto)
        #texto_dinheiro_ganhador = font_32.render(str("Saldo: " + str(dinheiro)), True, preto)
        #imagem_ganhador_final = eval("imagem_" + str(imagem_ganhador) + "_r")
        voltar = pygame.Rect((largura // 100) * 10, (altura // 100) * 70, 100, 36)

        # blit
        tela_6.blit(wallpaper_r, (0, 0))
        #tela_6.blit(imagem_ganhador_final, (400, 200))
        tela_6.blit(texto_nome_jogo, ((largura // 100) * 40, altura // 9))
        pygame.draw.rect(tela_6, branco, voltar)
        contador=1
        contador_altura = 10
        for blittop in range(10):
            nome_player = eval("texto_nome_" + str(contador))
            tela_6.blit(nome_player, ((largura // 100) * 10, (altura // 100) * contador_altura))  # nome
            contador += 1
            nome_player = eval("texto_nome_" + str(contador))
            tela_6.blit(nome_player, ((largura // 100) * 20, (altura // 100) * contador_altura))  # saldo
            contador += 1
            contador_altura +=5
        tela_6.blit(texto_botao_2, ((largura // 100) * 10, (altura // 100) * 70))  # ranking
        #tela_6.blit(texto_nome_ganhador, (100, 100))  # ranking
        #tela_6.blit(texto_dinheiro_ganhador, (200, 200))  # ranking

        pygame.display.update()

###parametros
largura = 1920
altura = 1080
px = (largura//100) * 2 #onde a janela vai aparecer em relativo a posição x
py = (altura//100) * 5 # onde a janela vai aparecer em relativo a posição y
#posicoes = [1] #lista com as pisoções das peças
posicoes = [[130, 680], [240, 680], [340, 680], [445, 680], [555, 680], [660, 680], [770, 680], [870, 680],[970, 680], [1080, 680], [1180, 680], [1280, 680]
        , [1280, 500], [1180, 500], [1080, 500], [970, 500], [870, 500], [770, 500], [660, 500], [555, 500], [445, 500],[340, 500], [240, 500], [130, 500], [45, 500]
        , [45, 310], [130, 310], [240, 310], [340, 310], [445, 310], [555, 310], [660, 310], [770, 310], [870, 310],[970, 310], [1080, 310], [1180, 310], [1280, 310]
        , [1280, 120], [1180, 120], [1080, 120], [970, 120], [870, 120], [770, 120], [660, 120], [555, 120], [445, 120],[340, 120], [240, 120], [130, 120], [45, 120]]
lista_boa = [1,8,13,15,16,23,24,26,31,32]
lista_ruim = [3,7,18,21,22,28,38,40,41,46]
fim = 51

#importando imagens
tabuleiro = pygame.image.load("TABULEIRO.png")
fundo_score = pygame.image.load("fundo_score.jpg")
fundo = pygame.image.load("fenda_do_bikini.jpg")
fundo_r = pygame.transform.scale(fundo, ((largura-(px*2)), (altura-(py*2))))
roleta_1 = pygame.image.load("roleta_1.png")
roleta_2 = pygame.image.load("roleta_2.png")
roleta_3 = pygame.image.load("roleta_3.png")
roleta_4 = pygame.image.load("roleta_4.png")
roleta_5 = pygame.image.load("roleta_5.png")
roleta_6 = pygame.image.load("roleta_6.png")

imagem_1 = pygame.image.load("1_bob_esponja.png")
imagem_1_r = pygame.transform.scale(imagem_1, (100,100))
imagem_1_r2 = pygame.transform.scale(imagem_1, (50,50))
imagem_2 = pygame.image.load("2_sandy.png")
imagem_2_r = pygame.transform.scale(imagem_2, (100,100))
imagem_2_r2 = pygame.transform.scale(imagem_2, (50,50))
imagem_3 = pygame.image.load("3_gary.png")
imagem_3_r = pygame.transform.scale(imagem_3, (100,100))
imagem_3_r2 = pygame.transform.scale(imagem_3, (50,50))
imagem_4 = pygame.image.load("4_sirigueijo.png")
imagem_4_r = pygame.transform.scale(imagem_4, (100,100))
imagem_4_r2 = pygame.transform.scale(imagem_4, (50,50))
imagem_5 = pygame.image.load("5_patrick.png")
imagem_5_r = pygame.transform.scale(imagem_5, (100,100))
imagem_5_r2 = pygame.transform.scale(imagem_5, (50,50))
imagem_6 = pygame.image.load("6_lula.png")
imagem_6_r = pygame.transform.scale(imagem_6, (100,100))
imagem_6_r2 = pygame.transform.scale(imagem_6, (50,50))
imagem_0 = pygame.image.load("nada.png")
imagem_0_r = pygame.transform.scale(imagem_0, (100,100))
imagem_0_r2 = pygame.transform.scale(imagem_0, (50,50))

wallpaper = pygame.image.load("./teste/wallpaper_tela_1.jpg")
wallpaper_r = pygame.transform.scale(wallpaper, ((largura-(px*2)), (altura-(py*2))))
lista_roleta = [roleta_1,roleta_2,roleta_3,roleta_4,roleta_5,roleta_6]

#cores
preto = (0,0,0)
branco = (255,255,255)
verde = (0,255,0)
vermelho = (255,0,0)
azul = (0,0,255)
botao_normal = (100,100,100)
botao_aceso = (170,170,170)

#setando objetos
pygame.init() # inicia biblioteca pygame
from pygame import mixer
mixer.init()
mixer.music.load('musiquinha_top.wav')

font_16 = pygame.font.Font('freesansbold.ttf',16)
font_28 = pygame.font.Font('freesansbold.ttf',28)
font_nome_game = pygame.font.Font('freesansbold.ttf',56)
font_56 = pygame.font.Font('freesansbold.ttf',56)
font_32 = pygame.font.Font('freesansbold.ttf',int(largura // 100 * 1.7))
font_35 = pygame.font.SysFont('Corbel',35)

import os # import os modulo
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (px, py) #magica da posição
tela_inicial() # chama o pre_jogo()