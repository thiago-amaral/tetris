import pygame as pg
import sys
from game import Game
from constants import *

pg.init()
screen = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption("Tetris!")
clock = pg.time.Clock()

def play():
    title_font = pg.font.Font(None, 40)
    label_font = pg.font.Font(None, 25)

    score_surface = title_font.render("Score", True, WHITE)
    lines_surface = title_font.render("Lines", True, WHITE)
    next_surface = title_font.render("Next", True, WHITE)
    game_over_surface = title_font.render("Game Over!", True, WHITE)

    group_surface = label_font.render("Group 35", True, WHITE)
    level_surface = label_font.render("1x Speed", True, WHITE)
    mode_surface = label_font.render("Normal Mode", True, WHITE)
    player_surface = label_font.render("Human Player", True, WHITE)

    score_rect = pg.Rect(350, 55, 170, 60)
    lines_rect = pg.Rect(350, 180, 170, 60)

    # lines_rect = pg.Rect(350, 500, 170, 60)
    next_rect = pg.Rect(350, 320, 170, 180)

    game = Game()

    GAME_UPDATE = pg.USEREVENT
    pg.time.set_timer(GAME_UPDATE, FALL_SPEED)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if game.game_over == True:
                    game = Game()

                if event.key == pg.K_LEFT and game.game_over == False:
                    game.move_left()

                if event.key == pg.K_RIGHT and game.game_over == False:
                    game.move_right()

                if event.key == pg.K_DOWN and game.game_over == False:
                    game.move_down()

                if event.key == pg.K_UP and game.game_over == False:
                    game.rotate()

                if event.key == pg.K_ESCAPE:
                    confirm()

            if event.type == GAME_UPDATE and game.game_over == False:
                game.move_down()

        score_val_surface = title_font.render(str(game.score), True, WHITE)
        lines_val_surface = title_font.render(str(game.lines), True, WHITE)

        screen.fill(DARK_BLUE)
        screen.blit(score_surface, (400, 20, 50, 50))
        screen.blit(lines_surface, (400, 150, 50, 50))
        screen.blit(next_surface, (400, 290, 50, 50))
        
        if game.game_over:
            screen.blit(game_over_surface, (360, 535, 50, 50))
        else:
            screen.blit(group_surface, (385, 515, 50, 50))
            screen.blit(level_surface, (385, 535, 50, 50))
            screen.blit(mode_surface, (385, 555, 50, 50))
            screen.blit(player_surface, (385, 575, 50, 50))

        pg.draw.rect(screen, LIGHT_BLUE, score_rect, 0, 10)
        pg.draw.rect(screen, LIGHT_BLUE, lines_rect, 0, 10)
        screen.blit(score_val_surface, score_val_surface.get_rect(centerx = score_rect.centerx, 
                                                                  centery = score_rect.centery))
        
        screen.blit(lines_val_surface, lines_val_surface.get_rect(centerx = lines_rect.centerx, 
                                                                  centery = lines_rect.centery))
        pg.draw.rect(screen, LIGHT_BLUE, next_rect, 0, 10)
        game.draw(screen)

        pg.display.update() # draws everything on screen object
        clock.tick(FRAMERATE) # display screen at 60 fps

def menu():
    title_font = pg.font.Font(None, 40)
    title_surface = title_font.render("Tetris", True, WHITE)

    label_font = pg.font.Font(None, 25)

    play_surface = label_font.render("Play", True, WHITE)
    play_rect = play_surface.get_rect(center=(290, 150))

    h_scores_surface = label_font.render("High Scores", True, WHITE)
    h_scores_rect = play_surface.get_rect(center=(260, 200))

    config_surface = label_font.render("Configurations", True, WHITE)
    config_rect = play_surface.get_rect(center=(250, 250))

    quit_surface = label_font.render("Quit", True, WHITE)
    quit_rect = play_surface.get_rect(center=(290, 300))


    course_surface = label_font.render("2023 2805ICT", True, WHITE)
    course_rect = play_surface.get_rect(center=(250, 400))

    author1_surface = label_font.render("Thiago Guerino Amaral (s5286821)", True, WHITE)
    author1_rect = play_surface.get_rect(center=(180, 440))

    author2_surface = label_font.render("Won Ki Kim (s5289094)", True, WHITE)
    author2_rect = play_surface.get_rect(center=(220, 470))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if play_rect.collidepoint(event.pos):
                        play()

                    if quit_rect.collidepoint(event.pos):
                        pg.quit()
                        sys.exit()

                    if h_scores_rect.collidepoint(event.pos):
                        high_scores()

                    if config_rect.collidepoint(event.pos):
                        configs()

        screen.fill(DARK_BLUE)
        screen.blit(title_surface, (250, 20, 50, 50))
        screen.blit(play_surface, play_rect)
        screen.blit(h_scores_surface, h_scores_rect)
        screen.blit(config_surface, config_rect)
        screen.blit(quit_surface, quit_rect)
        screen.blit(course_surface, course_rect)
        screen.blit(author1_surface, author1_rect)
        screen.blit(author2_surface, author2_rect)

        pg.display.update() # draws everything on screen object
        clock.tick(FRAMERATE) # display screen at 60 fps

def high_scores():
    title_font = pg.font.Font(None, 40)

    title_surface = title_font.render("Top 10 High Scores", True, WHITE)
    title_rect = title_surface.get_rect(center=(300, 50))

    human_surface = title_font.render("Human", True, WHITE)
    human_rect = human_surface.get_rect(center=(100, 100))

    ai_surface = title_font.render("AI", True, WHITE)
    ai_rect = ai_surface.get_rect(center=(450, 100))

    label_font = pg.font.Font(None, 25)

    back_surface = title_font.render("Back to Menu", True, WHITE)
    back_rect = back_surface.get_rect(center=(300, 500))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if back_rect.collidepoint(event.pos):
                        menu()

        screen.fill(DARK_BLUE)
        screen.blit(title_surface, title_rect)
        screen.blit(human_surface, human_rect)
        screen.blit(ai_surface, ai_rect)
        screen.blit(back_surface, back_rect)

        i = 0
        for name in ['Jack', 'John', 'James', 'George', 'Lucas', 'Paul', 'Carlos', 'Karl', 'Matt', 'Tim']:
            surface = label_font.render(f'{name}: {9678 - (i * 100)}', True, WHITE)
            rect = surface.get_rect(center=(100, 150 + (i * 30)))
            screen.blit(surface, rect)
            i += 1


        i = 0
        for i in range(10):
            surface = label_font.render(f'AI: {10238 - (i * 100)}', True, WHITE)
            rect = surface.get_rect(center=(450, 150 + (i * 30)))
            screen.blit(surface, rect)
            i += 1

        pg.display.update() # draws everything on screen object
        clock.tick(FRAMERATE) # display screen at 60 fps

def configs():
    title_font = pg.font.Font(None, 40)

    title_surface = title_font.render("Settings", True, WHITE)
    title_rect = title_surface.get_rect(center=(300, 50))

    label_font = pg.font.Font(None, 25)

    size_s = label_font.render("Size of the field: 10 x 20", True, WHITE)
    size_r = size_s.get_rect(center=(300, 150))

    level_s = label_font.render("Speed Level: 1x", True, WHITE)
    level_r = level_s.get_rect(center=(300, 200))

    mode_s = label_font.render("Game Mode: Normal", True, WHITE)
    mode_r = mode_s.get_rect(center=(300, 250))

    player_type_s = label_font.render("Player Type: Human", True, WHITE)
    player_type_r = player_type_s.get_rect(center=(300, 300))

    back_surface = title_font.render("Back to Menu", True, WHITE)
    back_rect = back_surface.get_rect(center=(300, 500))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if back_rect.collidepoint(event.pos):
                        menu()

        screen.fill(DARK_BLUE)
        screen.blit(title_surface, title_rect)
        screen.blit(size_s, size_r)
        screen.blit(level_s, level_r)
        screen.blit(mode_s, mode_r)
        screen.blit(player_type_s, player_type_r)
        screen.blit(back_surface, back_rect)

        

        pg.display.update() # draws everything on screen object
        clock.tick(FRAMERATE) # display screen at 60 fps

def confirm():
    title_font = pg.font.Font(None, 40)

    title_surface = title_font.render("Exit Game?", True, WHITE)
    title_rect = title_surface.get_rect(center=(300, 50))

    label_font = pg.font.Font(None, 25)

    msg_s = label_font.render("Are you sure you want to quit?", True, WHITE)
    msg_r = msg_s.get_rect(center=(280, 150))

    yes_s = title_font.render("Yes", True, WHITE)
    yes_r = yes_s.get_rect(center=(240, 230))

    no_s = title_font.render("No", True, WHITE)
    no_r = no_s.get_rect(center=(340, 230))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if yes_r.collidepoint(event.pos):
                        menu()
                    if no_r.collidepoint(event.pos):
                        return

        screen.fill(DARK_BLUE)
        screen.blit(title_surface, title_rect)
        screen.blit(msg_s, msg_r)
        screen.blit(yes_s, yes_r)
        screen.blit(no_s, no_r)

        pg.display.update() # draws everything on screen object
        clock.tick(FRAMERATE)

menu()