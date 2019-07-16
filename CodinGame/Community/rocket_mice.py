#!/usr/bin/env python3

Dir = {'W': (-1,0), 'E': (1,0), 'S': (0,1), 'N': (0,-1)}
ArrowsPerPlayer = 3
MouseScore = 1
CatScore = -10
CatFreq = 10


class Cell:
    def __init__(self):
        self.Mice = []
        self.Cats = []

    def clear(self):
        self.Mice.clear()
        self.Cats.clear()


class Simulator:
    def __init__(self):
        self.width, self.height = map(int,input().split())
        self.players_cnt = int(input())
        self.arrows_max_cnt = ArrowsPerPlayer * self.players_cnt
        self.doors_cnt = int(input())
        self.turns_cnt = int(input())
        self.Map = self.new_map()
        self.Pits = [(0,0), (self.width-1,0), (0,self.height-1), (self.width-1,self.height-1)]
        self.Players = [tuple(map(int,input().split())) for _ in range(self.players_cnt)]
        self.Scores = [0]*self.players_cnt
        self.Doors = []
        for _ in range(self.doors_cnt):
            coord,wall = input().split()
            coord = int(coord)
            if wall=='N':
                p = coord, 0
                d = Dir['S']
            elif wall=='S':
                p = coord, self.height-1
                d = Dir['N']
            elif wall=='E':
                p = self.width-1, coord
                d = Dir['W']
            elif wall=='W':
                p = 0, coord
                d = Dir['E']
            self.Doors.append((p,d))
        self.Arrows = []
        for _ in range(self.turns_cnt):
            x,y,d = input().split()
            p = int(x),int(y)
            d = Dir[d]
            self.Arrows.append((p,d))

    def cell_range(self):
        for x in range(self.width):
            for y in range(self.height):
                yield x,y

    def new_map(self):
        return [[Cell() for _ in range(self.height)] for _ in range(self.width)]

    def inside(self, x, y):
        return 0<=x<self.width and 0<=y<self.height

    def rotate(self, x, y):
        return y,-x

    def run(self):
        for self.curr_turn in range(self.turns_cnt+1):
            self.step()

    def move_animals(self, SrcMap, DstMap):
        for x,y in self.cell_range():
            for dx,dy in SrcMap[x][y].Mice:
                while not self.inside(x+dx,y+dy):
                    dx,dy = self.rotate(dx,dy)
                DstMap[x+dx][y+dy].Mice.append((dx,dy))
        for x,y in self.cell_range():
            for dx,dy in SrcMap[x][y].Cats:
                while not self.inside(x+dx,y+dy):
                    dx,dy = self.rotate(dx,dy)
                DstMap[x][y].Mice = [dxy for dxy in DstMap[x][y].Mice if dxy!=(-dx,-dy)]  # mice eaten in passing
                DstMap[x+dx][y+dy].Cats.append((dx,dy))

    def add_new_animals(self, Map):
        new_cat = ((self.curr_turn+1) % CatFreq == 0)
        for (x,y),d in self.Doors:
            (Map[x][y].Cats if new_cat else Map[x][y].Mice).append(d)

    def clear_pits(self, Map):
        for x,y in self.Pits:
            Map[x][y].clear()

    def update_score(self, player, score):
        self.Scores[player] = max(0, self.Scores[player] + score)

    def rocket_scores(self, Map):
        for i,(x,y) in enumerate(self.Players):
            self.update_score(i, len(Map[x][y].Mice)*MouseScore + len(Map[x][y].Cats)*CatScore)
            Map[x][y].clear()

    def eat_mice(self, Map):
        for x,y in self.cell_range():
            if Map[x][y].Cats:
                Map[x][y].Mice.clear()

    def curr_arrows(self):
        return self.Arrows[max(0,self.curr_turn-self.arrows_max_cnt) : self.curr_turn]

    def redirect_animals(self, Map):
        for (x,y),d in self.curr_arrows():
            Map[x][y].Mice = [d]*len(Map[x][y].Mice)
            Map[x][y].Cats = [d]*len(Map[x][y].Cats)

    def step(self):
        NewMap = self.new_map()
        self.move_animals(self.Map, NewMap)
        self.add_new_animals(NewMap)
        self.clear_pits(NewMap)
        self.rocket_scores(NewMap)
        if self.curr_turn==self.turns_cnt:  # last turn
            return
        self.eat_mice(NewMap)
        self.redirect_animals(NewMap)
        self.Map = NewMap


if __name__=='__main__':
    S = Simulator()
    S.run()
    for s in S.Scores:
        print(s)
