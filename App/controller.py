﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    """
    llamada la funcion de Inicialización del catalogo
    """
    catalog = model.newCatalog()
    return catalog


# Funciones para la carga de datos
def loadData(catalog):
    """
    carga los datos de los archivos en la estructura de datos
    """
    loadVideos(catalog)
    loadCategory(catalog)
    

def loadVideos(catalog):
    videosfile = cf.data_dir + 'Kaggle/videos-small.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addvideo(catalog, video) 
        
            
def loadCategory(catalog):
    categoryfile = cf.data_dir + 'Kaggle/category-id.csv'
    input_file = csv.DictReader(open(categoryfile, encoding='utf-8'))
    for category in input_file:
        model.addcategory(catalog, category)
        

   
    

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
