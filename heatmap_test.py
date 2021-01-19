import dash
import dash_core_components as dcc
import dash_html_components as html
import sd_material_ui
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

app = dash.Dash(
    __name__,
    external_stylesheets=[
        'https://fonts.googleapis.com/icon?family=Material+Icons',
        'https://fonts.googleapis.com/css2?family=Amaranth&family=Lato:wght@300;400&display=swap',
    ]
)

app.scripts.config.serve_locally = True

spacer = html.Div(children=[], style=dict(height=20, width=50))
final_spacer = html.Div(children=[], style=dict(height=400))

app.layout = html.Div(children=[
    sd_material_ui.Paper(children=[
    html.Div(className="row", children=[

        html.Div(className="col", children=[
            sd_material_ui.Subheader(['Sample Graph']),
            html.Div([
                dcc.Graph(id='graph-with-slider'),
            ]),
        ]),

        html.Div(className="col", children=[
            sd_material_ui.Button(children='Test',
                id='button1',
                disableShadow=False,
                useIcon=False,
                variant='contained',
                color="primary",),
            
            spacer,
            
            html.Div(children=[
                sd_material_ui.DropDownMenu(
                        id='dropdown-input',
                        labelText='Test',
                        labelId='dropdown-label',
                        value=1,
                        useGrouping=True,
                        variant="outlined",
                        options=[
                            dict(grouping='Group A'),
                            dict(primaryText='Option 1', value=1),
                            dict(primaryText='Option 2', value=2),
                            dict(grouping='Group B'),
                            dict(primaryText='Option 3', value=3),
                            dict(grouping='Group C'),
                            dict(primaryText='Option 4', value=4),
                        ])
                    ],
                style={'width': 200}),

            html.P(id='dropdown-output', style={"fontFamily": "Amaranth", "fontWeight": "normal"}),
            
            spacer,
            
            sd_material_ui.Slider(
                id='test-slider',
                valueLabelDisplay="auto",
                min=df['year'].min(),
                max=df['year'].max(),
                value=df['year'].min(),
                marks=[{'value': year, 'label': str(year)} for year in df['year'].unique()],
            ),

            spacer,

            sd_material_ui.ColorPicker(id='colorpicker-input'),
            html.Div(id="colorpicker-output")

    ]),

])]),

    spacer,

    html.Div(className="row", children=[
        sd_material_ui.Paper(className="col", children=[
            html.Div(children=[
                dcc.Graph(id='graph-with-slider-2'),
            ]),
        ]),
        sd_material_ui.Paper(className="col", children=[
        html.Div(children=[
            dcc.Graph(id='graph-with-slider-3'),
        ]),]),
    ]),

])

@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('test-slider', 'value'))
def update_figure(selected_year):
    print(selected_year)

    filtered_df = df[df.year == int(selected_year)]

    # print(filtered_df.year.dtypes, type(selected_year))

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     size="pop", hover_name="country",
                     log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig

@app.callback(
    dash.dependencies.Output('dropdown-output', 'children'),
    [dash.dependencies.Input('dropdown-input', 'value')])
def dropdown_callback(value):
    return ['Selection is: {}'.format(value)]

@app.callback(
    Output('colorpicker-output', 'children'),
    Input('colorpicker-input', 'value')
)
def colorpicker_callback(value):
    return value

if __name__ == '__main__':
    app.run_server(debug=True)