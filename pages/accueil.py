from dash import html
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash import html, dcc
import dash_bootstrap_components as dbc


dash.register_page(__name__, path="/", name="Accueil") # path = url (voir fichier app.py)

layout = html.Div(
    style={'textAlign': 'center', 'padding': '50px', 'background': '#3578bf',  # Chemin relatif de votre image d'arrière-plan
        'backgroundSize': 'cover',},
    children=[
        html.H1("Application de l'inititation à Git/ Github", style={'fontSize': '2.5em', 'color': 'white'}),
        
        html.P("Auteurs : TSINA Solène, HUYNH Phan Phuong Khanh, PETIO Solene", style={'fontSize': '1em', 'color': 'white'}),
        
    dbc.Row([       
        html.P("""Dire quelque trucs pour l'intro.""",
            style={'fontSize': '1.2em', 'color': "white", "text-align":"center"})
        ]) ,
    ]
)