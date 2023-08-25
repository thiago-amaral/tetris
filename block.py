import pygame as pg
from constants import BLOCK_COLORS


class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.col_offset = 0
        self.rotation_state = 0
        

    def move(self, rows, cols):
        self.row_offset += rows
        self.col_offset += cols

    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for pos in tiles:
            position = {'x': pos['x'] + self.row_offset, 'y': pos['y'] + self.col_offset}
            moved_tiles.append(position)
        return moved_tiles
    
    def rotate(self):
        self.rotation_state += 1

        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state == -1:
            self.rotation_state = len(self.cells) - 1

    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pg.Rect(offset_y + tile['y'] * self.cell_size, offset_x + tile['x'] * self.cell_size, self.cell_size - 1, self.cell_size - 1)
            pg.draw.rect(screen, BLOCK_COLORS[self.id], tile_rect)