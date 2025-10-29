"""
Funciones auxiliares para análisis de hábitats en Menorca.
Incluye funciones para visualización, lectura de datos y utilidades generales.
"""

import json
import geopandas as gpd
import matplotlib.pyplot as plt
import plotly.express as px


def load_geojson(filepath):
    """
    Carga un archivo GeoJSON y retorna un GeoDataFrame.
    
    Args:
        filepath (str): Ruta al archivo GeoJSON
        
    Returns:
        gpd.GeoDataFrame: Datos espaciales cargados
    """
    return gpd.read_file(filepath)


def plot_habitat_map(gdf, column=None, title="Mapa de Hábitats"):
    """
    Visualiza un mapa de hábitats usando plotly.
    
    Args:
        gdf (gpd.GeoDataFrame): GeoDataFrame con datos espaciales
        column (str, optional): Columna para colorear
        title (str): Título del mapa
        
    Returns:
        plotly.graph_objects.Figure: Figura interactiva
    """
    fig = px.choropleth_mapbox(
        gdf,
        geojson=gdf.geometry,
        locations=gdf.index,
        color=column,
        title=title,
        mapbox_style="open-street-map",
        hover_name=gdf.index
    )
    return fig


def prepare_data(gdf):
    """
    Prepara los datos para análisis.
    
    Args:
        gdf (gpd.GeoDataFrame): GeoDataFrame original
        
    Returns:
        gpd.GeoDataFrame: Datos preparados
    """
    gdf = gdf.copy()
    gdf = gdf.dropna(subset=['geometry'])
    return gdf
