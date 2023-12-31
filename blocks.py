from block import Block

class LBlock(Block):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            0: [{'x': 0, 'y': 2}, {'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}],
            1: [{'x': 0, 'y': 1}, {'x': 1, 'y': 1}, {'x': 2, 'y': 1}, {'x': 2, 'y': 2}],
            2: [{'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}, {'x': 2, 'y': 0}],
            3: [{'x': 0, 'y': 0}, {'x': 0, 'y': 1}, {'x': 1, 'y': 1}, {'x': 2, 'y': 1}],
        }

        self.move(0, 3)

class JBlock(Block):
    def __init__(self):
        super().__init__(id = 2)
        self.cells = {
            0: [{'x': 0, 'y': 0}, {'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}],
            1: [{'x': 0, 'y': 1}, {'x': 0, 'y': 2}, {'x': 1, 'y': 1}, {'x': 2, 'y': 1}],
            2: [{'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}, {'x': 2, 'y': 2}],
            3: [{'x': 0, 'y': 1}, {'x': 1, 'y': 1}, {'x': 2, 'y': 0}, {'x': 2, 'y': 1}],
        }

        self.move(0, 3)

class IBlock(Block):
    def __init__(self):
        super().__init__(id = 3)
        self.cells = {
            0: [{'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}, {'x': 1, 'y': 3}],
            1: [{'x': 0, 'y': 2}, {'x': 1, 'y': 2}, {'x': 2, 'y': 2}, {'x': 3, 'y': 2}],
            2: [{'x': 2, 'y': 0}, {'x': 2, 'y': 1}, {'x': 2, 'y': 2}, {'x': 2, 'y': 3}],
            3: [{'x': 0, 'y': 1}, {'x': 1, 'y': 1}, {'x': 2, 'y': 1}, {'x': 3, 'y': 1}],
        }

        self.move(-1, 3)

class OBlock(Block):
    def __init__(self):
        super().__init__(id = 4)
        self.cells = {
            0: [{'x': 0, 'y': 0}, {'x': 0, 'y': 1}, {'x': 1, 'y': 0}, {'x': 1, 'y': 1}]
        }

        self.move(0, 4)

class SBlock(Block):
    def __init__(self):
        super().__init__(id = 5)
        self.cells = {
            0: [{'x': 0, 'y': 1}, {'x': 0, 'y': 2}, {'x': 1, 'y': 0}, {'x': 1, 'y': 1}],
            1: [{'x': 0, 'y': 1}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}, {'x': 2, 'y': 2}],
            2: [{'x': 1, 'y': 1}, {'x': 1, 'y': 2}, {'x': 2, 'y': 0}, {'x': 2, 'y': 1}],
            3: [{'x': 0, 'y': 0}, {'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 2, 'y': 1}],
        }

        self.move(0, 3)

class TBlock(Block):
    def __init__(self):
        super().__init__(id = 6)
        self.cells = {
            0: [{'x': 0, 'y': 1}, {'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}],
            1: [{'x': 0, 'y': 1}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}, {'x': 2, 'y': 1}],
            2: [{'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}, {'x': 2, 'y': 1}],
            3: [{'x': 0, 'y': 1}, {'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 2, 'y': 1}],
        }

        self.move(0, 3)

class ZBlock(Block):
    def __init__(self):
        super().__init__(id = 7)
        self.cells = {
            0: [{'x': 0, 'y': 0}, {'x': 0, 'y': 1}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}],
            1: [{'x': 0, 'y': 2}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}, {'x': 2, 'y': 1}],
            2: [{'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 2, 'y': 1}, {'x': 2, 'y': 2}],
            3: [{'x': 0, 'y': 1}, {'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 2, 'y': 0}],
        }

        self.move(0, 3)