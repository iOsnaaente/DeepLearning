from matplotlib.image import imsave, imread
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw
import numpy as np

from threading import Thread, Lock
from time import time 

img_orig = Image.open('D:\Desktop\git\Algoritmo genético/meandlaula.png', 'r')
img_orig.thumbnail((250, 250))
y_hat = np.asarray(img_orig, dtype=int)[ :, :, :3 ]
BACKGROUND_COLOR = tuple( [ int(x) for x in np.mean( np.mean(y_hat, axis=0), axis=0) ] )
W, H, C = y_hat.shape


class Individuo ( Thread ):

    individual = tuple()
    score = []
    chr = []

    def __init__(self, chr, y_hat, score = None ):
        Thread.__init__(self)
        self.mutex = Lock()
        self.score = score
        self.y_hat = y_hat 
        self.chr   = chr 

    def get_phenotype(self, chromosome, triangles = 100):
        chromosome = chromosome.copy()
        img = Image.new('RGB', (H,W), BACKGROUND_COLOR )
        drw = ImageDraw.Draw(img,   'RGBA')

        for _ in range(triangles):
            triangle = list()
            for _ in range(3):
                x = chromosome.pop(0)
                y = chromosome.pop(0)
                triangle.append((y,x))
            r = chromosome.pop(0)
            g = chromosome.pop(0)
            b = chromosome.pop(0)
            a = chromosome.pop(0)
            drw.polygon(triangle, fill=(r,g,b,a) )
        return img
    
    def fitness(self, y, y_hat):
        diff = (y - y_hat)**2 
        err = np.sum(diff) / (y.shape[0]*y.shape[1]*y.shape[2])
        return err
    
    def compute_fitness(self, individual):
        if individual[1] is None:
            img = get_phenotype( individual[0] )
            y = np.asarray(img, dtype=int)
            score = fitness(y, y_hat)
            new_individual = (individual[0], score)
        return individual
    
    def run(self):
        pass 