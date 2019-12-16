import turtle
import quoridor

def tracerpolygone(jack, poly):
    "À l'aide de la tortue ronnie, tracer un polygone "
    jack.penup()
    jack.color('black')
    jack.width(3)
    jack.goto(poly[0])
    jack.pendown()
    for pos in poly[1:]:
        jack.goto(pos)


class QuoridorX(quoridor.Quoridor):
    """Ce module permet de faire l'affichage graphique du jeu Quoridor"""
    def __init__(self, joueurs, murs=None):
        super().__init__(joueurs, murs)
        ced = turtle.Turtle(visible=None)
        ced.shape(None)
        ced.speed(0)
        n = 35
        for i in range(10):
            tracerpolygone(ced, ((-(9-2*i)*n, -9*n), (-(9-2*i)*n, 9*n)))
            tracerpolygone(ced, ((9*n, -(9-2*i)*n), (-9*n, -(9-2*i)*n)))

        scr = turtle.Screen()
        scr.title('Quoridor')
        scr.bgcolor('red')
        scr.setup(width=22*n, height=22*n)
        
        self.yac = turtle.Turtle(shape='square')
        self.yac.penup()
        self.yac.shapesize(0.075*n)
        self.yac.color('black')
        self.yac.speed(0)
        self.yac.right(90)
        self.yac.forward(8*n)
        self.cha = turtle.Turtle(shape='circle')
        self.cha.penup()
        self.cha.shapesize(0.075*n)
        self.cha.color('black')
        self.cha.speed(0)
        self.cha.left(90)
        self.cha.forward(8*n)
        self.jac = turtle.Turtle(visible=None)
        self.jac.penup()

        for a in range(1, 10):
            self.jac.goto(-10*n+a*2*n, 9*n)
            self.jac.write(str(a), align='center', font=('arial', 27, 'bold'))
        for a in range(1, 10):
            self.jac.goto(-10*n, -11*n+3+2*n*a)
            self.jac.write(str(a), align='center', font=('arial', 27, 'bold'))
        self.afficher_graphe()

    def afficher_graphe(self):
        "permet d'afficher dans un fenetre graphique les actualisation du jeu"
        n = 35
        etat = self.état_partie()
        a = list(j for j in etat['joueurs'])

        self.yac.goto(-10*n + 2*n*(a[0]['pos'][0]), -10*n + 2*n*(a[0]['pos'][1]))
        self.cha.goto(-10*n + 2*n*(a[1]['pos'][0]), -10*n + 2*n*(a[1]['pos'][1]))

        for mur in etat['murs']['horizontaux']:
            emma = turtle.Turtle(visible=None)
            emma.pensize(0.6*n)
            emma.speed(0)
            emma.pencolor('white')
            emma.penup()
            emma.goto(-10.5*n+2*n*mur[0], -11*n+2*n*mur[1])
            emma.pendown()
            emma.forward(3*n)

        for mur in etat['murs']['verticaux']:
            drix = turtle.Turtle(visible=None)
            drix.pensize(0.6*n)
            drix.speed(0)
            drix.pencolor('white')
            drix.penup()
            drix.goto(-11*n+2*n*mur[0], -10.5*n+2*n*mur[1])
            drix.pendown()
            drix.left(90)
            drix.forward(3*n)


