import pygame
import time
pygame.init()

GAME_WINDOW = pygame.display.set_mode((312, 312))
pygame.display.set_caption("Tic TAc TOE By Zaber")

_white = (255, 255, 255)
_black = (0, 0, 0)

_grid = [[pygame.Rect(0, 0, 100, 100), pygame.Rect(106, 0, 100, 100), pygame.Rect(212, 0, 100, 100)],
         [pygame.Rect(0, 106, 100, 100), pygame.Rect(106, 106, 100, 100), pygame.Rect(212, 106, 100, 100)],
         [pygame.Rect(0, 212, 100, 100), pygame.Rect(106, 212, 100, 100), pygame.Rect(212, 212, 100, 100)]]
_turn = True #False=Cross and True=Circle
_player_grid = [[None, None, None],
                [None, None, None],
                [None, None, None]]
_moves = 0

CROSS = pygame.image.load("Cross.png")
CIRCLE = pygame.image.load("Circle.png")

_clock = pygame.time.Clock()
_fps = 30
_font = pygame.font.SysFont(None, 60)

def placeit(m_pos):
    global _turn, _moves
    
    _go_back = False
    for i in range(3):
        for j in range(3):
            if m_pos[0] < _grid[i][j].bottomright[0] and m_pos[1] < _grid[i][j].bottomright[1]:
                if _turn:
                    _player_grid[i][j] = True
                    _turn = False
                    _moves += 1
                    _go_back = True
                else:
                    _player_grid[i][j] = False
                    _turn = True
                    _moves += 1
                    _go_back = True
                break
        if _go_back: break
    return

def gameover(_cur_val = None):
    GAME_WINDOW.fill(_black)
    if _moves < 10:
        if _cur_val:
            _cir = _font.render("Circle Wins!", 1, _white)
            GAME_WINDOW.blit(_cir, [(GAME_WINDOW.get_width() / 2) - (_cir.get_width() / 2), (GAME_WINDOW.get_height() / 2) - (_cir.get_height() / 2)])
        else:
            _cro = _font.render("Cross Wins!", 1, _white)
            GAME_WINDOW.blit(_cro, [(GAME_WINDOW.get_width() / 2) - (_cro.get_width() / 2), (GAME_WINDOW.get_height() / 2) - (_cro.get_height() / 2)])
    else:
        _tie = _font.render("No one won!", 1, _white)
        GAME_WINDOW.blit(_tie, [(GAME_WINDOW.get_width() / 2) - (_tie.get_width() / 2), (GAME_WINDOW.get_height() / 2) - (_tie.get_height() / 2)])
    pygame.display.update()
    time.sleep(5)
    return

def gameloop():
    _end_game = False
    
    while not _end_game:
        GAME_WINDOW.fill(_black)
        
        if _moves < 10:
            for i in range(3):
                for j in range(3):
                    pygame.draw.rect(GAME_WINDOW, _white, _grid[i][j])
                    if _player_grid[i][j] != None:
                        if _player_grid[i][j]: GAME_WINDOW.blit(CIRCLE, _grid[i][j])
                        else: GAME_WINDOW.blit(CROSS, _grid[i][j])
        else:
            _end_game = True
            gameover()
        
        pygame.display.update()
        
        _clock.tick(_fps)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                _end_game = True
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                placeit(pygame.mouse.get_pos())
        
        #Checking Horizontally.
        for i in range(3):
            _current_val = _player_grid[i][0]
            _cnt = 0
            for j in range(3):
                if _current_val != None:
                    if _player_grid[i][j] == _current_val:
                        _cnt += 1
                        if _cnt == 3:
                            _end_game = True
                            gameover(_current_val)
                            break
                    else: _cnt = 0
            if _cnt == 3: break
            
        #Checking Vertically.
        for j in range(3):
            _current_val = _player_grid[0][j]
            _cnt = 0
            for i in range(3):
                if _current_val != None:
                    if _player_grid[i][j] == _current_val:
                        _cnt += 1
                        if _cnt == 3:
                            _end_game = True
                            gameover(_current_val)
                            break
                    else: _cnt = 0
            if _cnt == 3: break
            
        #Checking Diagonally from Top-Left to Botton-Right.
        _current_val = _player_grid[0][0]
        _cnt = 0
        if _current_val != None:
            for i in range(3):
                j = i
                if _player_grid[i][j] == _current_val:
                    _cnt += 1
                    if _cnt == 3:
                        _end_game = True
                        gameover(_current_val)
                        break
                else: _cnt = 0
                    
        #Checking Diagonally from Bottom-Left to Top-Right.
        _current_val = _player_grid[2][0]
        _cnt = 0
        i = 2
        if _current_val != None:
            for j in range(3):
                if _player_grid[i][j] == _current_val:
                    _cnt += 1
                    i -= 1
                    if _cnt == 3:
                        _end_game = True
                        gameover(_current_val)
                        break
                else: _cnt = 0
    pygame.quit()
    return
gameloop()