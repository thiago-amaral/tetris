import random
from grid import Grid
from blocks import *

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.curr_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.lines = 0

    def update_score(self, lines_cleared):
        self.lines += lines_cleared

        if lines_cleared == 1:
            self.score += 100

        elif lines_cleared == 2:
            self.score += 300

        elif lines_cleared == 3:
            self.score += 600

        elif lines_cleared == 4:
            self.score += 1000

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]

        block = random.choice(self.blocks)
        self.blocks.remove(block)

        return block
    
    def move_left(self):
        self.curr_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.curr_block.move(0, 1)

    def move_right(self):
        self.curr_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.curr_block.move(0, -1)

    def move_down(self):
        self.curr_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.curr_block.move(-1, 0)
            self.lock_block()

    def rotate(self):
        self.curr_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.curr_block.undo_rotation()


    def lock_block(self):
        tiles = self.curr_block.get_cell_positions()
        for pos in tiles:
            self.grid.grid[pos['x']][pos['y']] = self.curr_block.id
        self.curr_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        self.update_score(rows_cleared)
        if self.block_fits() == False:
            self.game_over = True

    def block_fits(self):
        tiles = self.curr_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile['x'], tile['y']) == False:
                return False
        return True

    def block_inside(self):
        tiles = self.curr_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile['x'], tile['y']) == False:
                return False
        return True
    
    def draw(self, screen):
        self.grid.draw(screen)
        self.curr_block.draw(screen, 1, 1)
        self.next_block.draw(screen, 400, 300)