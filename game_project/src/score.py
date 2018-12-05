import pygame  as pg


class Score(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.font = pg.font.SysFont('Comic Sans MS', 40)
        self.font.set_italic(1)
        self.color = pg.Color('red')
        self.score = 0
        self.score_delta = 0
        self.image = self.font.render("Score: %d" % self.score, 0, self.color)
        self.update()
        self.rect = self.image.get_rect().move(0, 0)

    def update(self):
        if self.score_delta != 0:
            self.score += self.score_delta
            msg = "Score: %d" % self.score
            self.image = self.font.render(msg, 0, self.color)
            self.score_delta = 0

    def set_score_delta(self, delta):
        self.score_delta = delta
