import dash
from dash import dcc as dcc
from dash import html as html
import pandas as pd
import json
import plotly.express as px
from dash.dependencies import Input, Output, State
from search_data import search_data

# Load the existing data from the file
with open("data.txt", "r") as file:
    existing_data = json.load(file)

# Create a pandas dataframe from the data
df = pd.DataFrame(existing_data, columns=['FirstName', 'LastName', 'Email','Position', 'Company'])

# Define the Dash app
app = dash.Dash(__name__, assets_folder='assets')

# Define the layout for the homepage
home_layout = html.Div([
    
    html.Div(className='container', children=[
         html.H1("Welcome to A.D.A.M.S DataSphere DashBoard"),
         html.P("DataSphere is a visual platform for displaying, analyzing, and visualzing data. With A.D.A.M.S & DataSphere, you can easily upload data, search, analzye, and create visualizations to share with others."),
         html.H2("Getting Started"),
         html.P("To get started, you can either upload your own data or search the existing data. Use the links below to navigate the site.\n Please use if issues occur running the page:   kill -9 $(ps -A | grep python | awk '{print $1}')"), 
         html.H2("What can you do with DataSphere"),
         html.Ul([
            html.Li("Store and manage your data"),
            html.Li("Search and filter your data"),
            html.Li("Visualize your data with graphs and charts"),
            html.Li("Export your data to CSV"),
            html.Li("Share your data with others"),
            
         ]),
         html.Hr(),
         html.P("Ready to get started? Choose an Option on the left hand")
         ]),
    ])

# Define the layout for the analysis page
analysis_layout = html.Div([
    html.H1("Data Analysis"),
    dcc.Graph(
        id="Position-counts",
        figure=px.bar(df, x='Position', title='Entries by Position', color='Position').update_layout(showlegend=False)
    ),
    dcc.Graph(
        id="Company-counts",
        figure=px.bar(df, x='Company', title='Entries by Company', color='Company').update_layout(showlegend=False)
    ),

    dcc.Graph(
        id="Position-counts",
        figure=px.histogram(df, x='FirstName', title='FirstName', color='Position').update_layout(showlegend=True)
    ),
    dcc.Graph(
        id="-Company_counts",
        figure=px.histogram(df, x='Company', title='Entries by Company', color='Company').update_layout(showlegend=True)
    )
]),

# Define the layout for the search page
search_layout = html.Div([
    html.H1("Data Search"),
    dcc.Input(
        id="search-input",
        type="text",
        placeholder="Enter search term..."
    ),
    html.Button(
        id="search-button",
        children="Search",
        n_clicks = 0
    ),
    html.Div(
        id="search-results"
    )
]),

display_layout = html.Div([
    html.H1("All Data"),
    html.P("Below all uploaded data will be displayed. Ctrl + F for quick search"),
    html.Script(src="assets/sort.js"),
    html.Table([
        html.Thead(html.Tr([html.Th(col) for col in df.columns])),
        html.Tbody([
            html.Tr([
                html.Td(df.iloc[i][col]) for col in df.columns
            ]) for i in range(len(df))
        ])
    ])
])

# Define the callback for the search button
@app.callback(
    Output("search-results", "children"),
    Input("search-button", "n_clicks"),
    State("search-input", "value")
)

def search_callback(n_clicks, search_term):
    if search_term:
        results = search_data(search_term)
        if results:
            return html.Table([
                html.Thead(html.Tr([html.Th(col) for col in df.columns])),
                html.Tbody([
                    html.Tr([
                        html.Td(results[i][col]) for col in df.columns
                    ]) for i in range(len(results))
                ])
            ])
        else:
            return html.Div("No results found.")
    else:
        return html.Div()

# Define the app layout
app.layout = html.Div([
    html.Img(src="assets/logo.png", height=78),
    html.Br(),
    dcc.Location(id="url"),
    dcc.Link("Homepage",href="/homepage"),
    html.Br(),
    dcc.Link("Analysis", href="/analysis"),
    html.Br(),
    dcc.Link("Search", href="/search"),
    html.Br(),
    dcc.Link("All data", href="/data"),
    html.Br(),
    html.Div(id="page-content")
])

# Define the callback for the page content
@app.callback(
Output("page-content", "children"),
Input("url", "pathname")
)
def display_page(pathname):
    if pathname == "/analysis":
        return analysis_layout
    elif pathname == "/search":
        return search_layout
    elif pathname == "/data":
        return display_layout
    else:
        return home_layout

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)