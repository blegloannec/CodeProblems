#!/usr/bin/env python3

from fractions import Fraction

class Ball:
    def __init__(self, x0, y0, vx, vy):
        self.x, self.y = Fraction(x0), Fraction(y0)
        self.vx, self.vy = Fraction(vx), Fraction(vy)

    def move(self, t):
        self.x += t * self.vx
        self.y += t * self.vy


class SegmentH:
    def __init__(self, x0, x1, y):
        self.x0,self.x1 = (x0,x1) if x0<x1 else (x1,x0)
        self.y = Fraction(y)

    def intersect(self, ball):
        if ball.vy!=0:
            t = (self.y-ball.y)/ball.vy
            if t>0:
                x = ball.x + t*ball.vx
                if self.x0<=x<=self.x1:
                    return t
        return None


class SegmentV:
    def __init__(self, x, y0, y1):
        self.x = Fraction(x)
        self.y0,self.y1 = (y0,y1) if y0<y1 else (y1,y0)

    def intersect(self, ball):
        if ball.vx!=0:
            t = (self.x-ball.x)/ball.vx
            if t>0:
                y = ball.y + t*ball.vy
                if self.y0<=y<=self.y1:
                    return t
        return None


class Box:
    # has 4 Sides N S W E
    def intersect(self, ball):
        idx = tmin = None
        for i in range(4):
            t = self.Sides[i].intersect(ball)
            if t is not None and (tmin is None or t<tmin):
                idx, tmin = i, t
        return idx,tmin


class Brick(Box):
    W, H = 100, 30
    def __init__(self, x, y, strength, points):
        self.x, self.y = x, y
        self.strength = strength
        self.points = points
        self.Sides = [SegmentH(x,x+self.W,y), SegmentH(x,x+self.W,y+self.H),  \
                      SegmentV(x,y,y+self.H), SegmentV(x+self.W,y,y+self.H)]

    def broken(self):
        return self.strength==0

    def hit(self):
        assert not self.broken()
        self.strength -= 1
        return self.points if self.strength==0 else 0


class Paddle(Box):
    W, H = 200, 3
    def __init__(self, Positions):
        self.pi = 0
        self.Pos = Positions
        self.up_sides()

    def up_sides(self):
        x,y = self.Pos[self.pi]
        self.Sides = [SegmentH(x,x+self.W,y), SegmentH(x,x+self.W,y+self.H),  \
                      SegmentV(x,y,y+self.H), SegmentV(x+self.W,y,y+self.H)]

    def hit(self):
        if self.pi+1<len(self.Pos):
            self.pi += 1
            self.up_sides()
        return 0


class Playfield(Box):
    W, H = 1600, 2400
    def __init__(self, Bricks, ball, paddle):
        self.Bricks = Bricks
        self.ball = ball
        self.paddle = paddle
        self.score = 0
        self.Sides = [SegmentH(0,self.W,0), SegmentH(0,self.W,self.H),  \
                      SegmentV(0,0,self.H), SegmentV(self.W,0,self.H)]

    def step(self):
        s,t = self.intersect(self.ball)
        Omin = None
        sp,tp = self.paddle.intersect(self.ball)
        if tp is not None and tp<t:
            Omin, s, t = self.paddle, sp, tp
        for B in self.Bricks:
            if not B.broken():
                sb, tb = B.intersect(self.ball)
                if tb is not None and tb<t:
                    Omin, s, t = B, sb, tb
        self.ball.move(t)
        if Omin is not None:
            self.score += Omin.hit()
        elif s==1:  # leaving S border of the field
            return False
        if s<2:  # horizontal wall
            self.ball.vy = -self.ball.vy
        else:
            self.ball.vx = -self.ball.vx
        return True

    def run(self):
        while self.step():
            pass
        return self.score


if __name__=='__main__':
    bx,by = map(int,input().split())
    vx,vy = map(int,input().split())
    Np = int(input())
    Nk = int(input())
    PadPos = [tuple(map(int,input().split())) for _ in range(Np)]
    Bricks = [Brick(*map(int,input().split())) for _ in range(Nk)]
    Game = Playfield(Bricks, Ball(bx,by,vx,vy), Paddle(PadPos))
    print(Game.run())
