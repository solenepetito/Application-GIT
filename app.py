from dash import html, Dash, page_registry, page_container
import dash_bootstrap_components as dbc


# Initialisation de l'application Dash
app = Dash(__name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.LUX]
)

# Barre de présentation avec logo et séparation
barre_pres = html.Div([
    html.Img(src='/assets/img/esg.png', className="logo", style={"width": "150px"}),  # Assurez-vous que l'image est dans assets/img
    html.Hr()  # Ligne horizontale pour séparer
])

# Barre latérale avec les liens de navigation
sidebar = dbc.Col(
    dbc.Nav([
        dbc.NavLink("Accueil", href="/", active="exact"),
        dbc.NavLink("Solène TSINA", href="/solene_t", active="exact"), 
        dbc.NavLink("Solène PETIO", href="/solene_p", active="exact"), 
        dbc.NavLink("Phan Phuong Khanh HUYNH", href="/khanh", active="exact"),
        # dbc.NavLink("Conclusion", href="/ccl", active="exact")
    ],
    vertical=True,
    pills=True),  # Style pills pour les liens
    width=2,  # Largeur de la barre latérale
    className='sidebar'
)

# Conteneur pour le contenu de la page
content = dbc.Col([html.Div(page_container, className='body')], width=10)

# Mise en page globale de l'application avec barre latérale et contenu
app.layout = dbc.Container([barre_pres, dbc.Row([sidebar, content])], fluid=True)


if __name__ == "__main__":
    app.run(debug=True)
