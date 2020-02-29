#encoding: utf-8

'''
Created on 28 feb. 2020

@author: Rod
'''

import random

class Movie(object):
    '''
    Clase Movie con atributos Title y Rank.
    '''

    def __init__(self, title):
        self.title = title.lower()
        self.rank = random.randint(0, 10)
    
    def like(self):
        '''
        Aumenta en 1 el Rank de la pelicula.
        '''
        self.rank += 1
    
    def dislike(self):
        '''
        Reduce en 1 el Rank de la pelicula.
        '''
        self.rank -= 1
    
    def display(self):
        '''
        Muestra el titulo de la pelicula con Mayuscula la primer letra de cada palabra y el rango.
        '''
        print("Título: %-30s Rango: %d" % (self.title.title(), self.rank))

movie1 = Movie('Marvellous')
movie2 = Movie('The Hot Chick')
movie3 = Movie('Little Chicken')
movie4 = Movie('Macario')
movie5 = Movie('El Escapulario')
movie6 = Movie('3 Idiots')
movie7 = Movie('Todas las Pecas del Mundo')
movie8 = Movie('Roma')
movie9 = Movie('El Laberinto del Fauno')
movie10 = Movie('El País del Miedo')

movies = [movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, movie9, movie10]

def imprimirMoviesAlfabeticamente(lista_movies):
    '''
    Método que permite imprimir en orden alfabético el listado
    de películas.
    '''
    lista_movies.sort(key=lambda x: x.title, reverse=False)
    
    archivo_movies = open("Archivos/movies_alpha.txt", "w")
    for movie in lista_movies:
        archivo_movies.write("Título: %-30s Rango: %-10s\n" % (movie.title.title(), movie.rank))

def imprimirMoviesPorRango(lista_movies):
    '''
    Método que permite imprimir en orden descendente el rango del listado
    de películas.
    '''
    lista_movies.sort(key=lambda x: x.rank, reverse=True)
    
    archivo_movies = open("Archivos/movies_rank.txt", "w")
    for movie in lista_movies:
        archivo_movies.write("Título: %-30s Rango: %-10s\n" % (movie.title.title(), movie.rank))

movie1.display()
movie1.like()
movie1.like()
movie1.like()
movie1.display()
movie1.dislike()
movie1.display()
print("---------------------")
movie5.display()
movie5.like()
movie5.like()
movie5.like()
movie5.display()
movie5.dislike()
movie5.dislike()
movie5.dislike()
movie5.dislike()
movie5.display()
print("---------------------")

imprimirMoviesAlfabeticamente(movies)
imprimirMoviesPorRango(movies)


        