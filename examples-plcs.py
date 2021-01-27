import dash
import dash_core_components as dcc
import dash_html_components as html
import sd_material_ui
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px

# df = pd.read_csv(
#     'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

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

sidebar = html.Div(className="sidebar-container", children=[
    html.Div(className="sidebar-header", children="Dashboard"),
    html.Div(className="sidebar-item", children="Dashboard A"),
    html.Div(className="sidebar-item selected", children="Dashboard B"),
    html.Div(className="sidebar-item", children="Dashboard C"),
])

app.layout = html.Div(className="main-container", children=[
    html.Div(className="body-container", children=[

        # Grid layout
        html.Div(className="row", children=[
            html.Div(className="col start", children=[
                     sd_material_ui.Paper(children="Equal width col - left aligned")]),
            html.Div(className="col center", children=[
                     sd_material_ui.Paper(children="Equal width col - middle aligned")]),
            html.Div(className="col end", children=[
                sd_material_ui.Paper(children="Equal width col - right aligned")]),
        ]),
        html.Div(className="row", children=[
            html.Div(className="col-4", children=[
                     sd_material_ui.Paper(children="Unequal Width Col 1")]),
            html.Div(className="col-8", children=[
                     sd_material_ui.Paper(children="Unequal Width Col 1")]),
        ]),
        html.Div(className="row", children=[
            html.Div(className="col col-offset-8", children=[
                     sd_material_ui.Paper(children="Column with offset")]),
        ]),

        # Typography
        html.Div(className="row", children=[
            html.Div(className="col col-4", children=[
                     sd_material_ui.Paper(children=[
                         html.H1(className="text-grey-one",
                                 children="Heading 1"),
                         html.H2(className="text-grey-one",
                                 children="Heading 2"),
                         html.P(className="body1 text-grey-one",
                                children="Body 1"),
                         html.P(className="body2 text-grey-one",
                                children="Body 2"),
                         html.P(className="body3 text-grey-one",
                                children="Body 3")
                     ])])
        ]),

        html.Div(className="row", children=[
            # Color Palette
            html.Div(className="col col-4", children=[
                sd_material_ui.Paper(children=[
                     html.H1(className="text-grey-one",
                             children="Color Palette"),
                     html.Div(
                         className="row", children=[
                             html.Div(className="col col-6 text-primary-main",
                                      children=".primary-main"),
                             html.Div(className="col col-6 bg-primary-main")
                         ]),
                     html.Div(
                         className="row", children=[
                             html.Div(className="col col-6 text-primary-dark",
                                      children=".primary-dark"),
                             html.Div(className="col col-6 bg-primary-dark")
                         ]),
                     html.Div(
                         className="row", children=[
                             html.Div(className="col col-6 text-primary-light",
                                      children=".primary-light"),
                             html.Div(className="col col-6 bg-primary-light")
                         ]),
                     html.Div(
                         className="row", children=[
                             html.Div(className="col col-6 text-primary-lighter",
                                      children=".primary-lighter"),
                             html.Div(className="col col-6 bg-primary-lighter")
                         ]),
                     ])]),
            html.Div(className="col col-4", children=[
                     sd_material_ui.Paper(children=[
                         html.H1(className="text-grey-one",
                                 children="Color Palette"),
                         html.Div(
                             className="row", children=[
                                 html.Div(className="col col-6 text-secondary-main",
                                          children=".secondary-main"),
                                 html.Div(
                                     className="col col-6 bg-secondary-main")
                             ]),
                         html.Div(
                             className="row", children=[
                                 html.Div(className="col col-6 text-secondary-dark",
                                          children=".secondary-dark"),
                                 html.Div(
                                     className="col col-6 bg-secondary-dark")
                             ]),
                         html.Div(
                             className="row", children=[
                                 html.Div(className="col col-6 text-secondary-light",
                                          children=".secondary-light"),
                                 html.Div(
                                     className="col col-6 bg-secondary-light")
                             ]),
                         html.Div(
                             className="row", children=[
                                 html.Div(className="col col-6 text-secondary-lighter",
                                          children=".secondary-lighter"),
                                 html.Div(
                                     className="col col-6 bg-secondary-lighter")
                             ]),
                     ])]),
            html.Div(className="col col-4", children=[
                sd_material_ui.Paper(children=[
                    html.H1(className="text-grey-one",
                                     children="Color Palette"),
                    html.Div(
                        className="row", children=[
                            html.Div(className="col col-6 text-grey-one",
                                     children=".grey-one"),
                            html.Div(
                                className="col col-6 bg-grey-one")
                        ]),
                    html.Div(
                        className="row", children=[
                            html.Div(className="col col-6 text-grey-two",
                                     children=".grey-two"),
                            html.Div(
                                className="col col-6 bg-grey-two")
                        ]),
                    html.Div(
                        className="row", children=[
                            html.Div(className="col col-6 text-grey-three",
                                     children=".grey-three"),
                            html.Div(
                                className="col col-6 bg-grey-three")
                        ]),
                    html.Div(
                        className="row", children=[
                            html.Div(className="col col-6 text-grey-four",
                                     children=".grey-four"),
                            html.Div(
                                className="col col-6 bg-grey-four")
                        ]),
                    html.Div(
                        className="row", children=[
                            html.Div(className="col col-6 text-grey-five",
                                     children=".grey-five"),
                            html.Div(
                                className="col col-6 bg-grey-five")
                        ]),
                    html.Div(
                        className="row", children=[
                            html.Div(className="col col-6 text-grey-six",
                                     children=".grey-six"),
                            html.Div(
                                className="col col-6 bg-grey-six")
                        ]),
                ])])
        ]),

        # Buttons
        html.Div(className="row", children=[
            html.Div(className="col col-6", children=[
                sd_material_ui.Paper(children=[
                    html.Div(className="row around", children=[
                        sd_material_ui.Button(
                            variant="contained", color="primary", children="Primary"),
                        sd_material_ui.Button(
                            variant="outlined", color="primary", children="Secondary"),
                        sd_material_ui.Button(
                            variant="text", color="primary", children="Tertiary")
                    ])
                ])

            ])
        ]),

        # Dropdown
        html.Div(className="row", children=[
            html.Div(className="col col-6", children=[
                sd_material_ui.Paper(children=[
                    html.Div(className="row around", children=[
                        sd_material_ui.DropDownMenu(
                            id='dropdown-input-1',
                            labelText='Simple Dropdown',
                            labelId='dropdown-label-1',
                            value=1,
                            variant="outlined",
                            options=[
                                dict(primaryText='Option 1', value=1),
                                dict(primaryText='Option 2', value=2),
                                dict(primaryText='Option 3', value=3),
                                dict(primaryText='Option 4', value=4),
                            ]),
                        sd_material_ui.DropDownMenu(
                            id='dropdown-input-2',
                            labelText='Grouped Dropdown',
                            labelId='dropdown-label-2',
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
                    ]),
                ])
            ])
        ]),

        # Checkbox
        html.Div(className="row", children=[
            html.Div(className="col col-6", children=[
                sd_material_ui.Paper(children=[
                    sd_material_ui.Checkbox(
                        id="checkbox-1", checked=True, label="Check")
                ])
            ])
        ]),

        # Slider
        html.Div(className="row", children=[
            html.Div(className="col col-6", children=[
                sd_material_ui.Paper(className="text-grey-one", children=[
                    html.H2(children="Slider"),
                    sd_material_ui.Slider(
                        id='slider-1',
                    ),
                    sd_material_ui.Slider(
                        id='slider-2',
                        valueLabelDisplay="auto",
                        min=0,
                        max=10,
                        value=5,
                    ),
                    sd_material_ui.Slider(
                        id='slider-3',
                        valueLabelDisplay="auto",
                        min=0,
                        max=10,
                        value=5,
                        marks=[{'value': i, 'label': i}
                               for i in range(11)],
                    ),
                    sd_material_ui.Slider(
                        id='slider-4',
                        valueLabelDisplay="auto",
                        value=[30, 70],
                    ),
                ])
            ])
        ]),

        # Color Picker
        html.Div(className="row", children=[
            html.Div(className="col col-6", children=[
                sd_material_ui.Paper(children=[
                    sd_material_ui.ColorPicker(
                        id="colorpicker-1")
                ])
            ])
        ]),

        # Graphs
        spacer,
        html.Div(className="row", children=[
            html.Div(className="col", children=[
                     sd_material_ui.Paper(children=[dcc.Graph(id='g-1')])]),
            html.Div(className="col", children=[
                     sd_material_ui.Paper(children=[dcc.Graph(id='g-2')])]),
        ]),
        spacer,
        html.Div(className="row", children=[
            html.Div(className="col col-4", children=[
                     sd_material_ui.Paper(children=[dcc.Graph(id='g-3')])]),
            html.Div(className="col col-8", children=[
                     sd_material_ui.Paper(children=[dcc.Graph(id='g-4')])]),
        ]),

        spacer,
        # Autocomplete
        html.Div(className="row", children=[
            html.Div(className="col col-4", children=[
                 sd_material_ui.Paper(children=[
                     sd_material_ui.AutoComplete(id="autocomplete-1", dataSource=[{"label": "Aa", "value": "aa"}, {
                                                 "label": "Ab", "value": "ab"}, {"label": "Ac", "value": "ac"}])
                 ])
                 ])
        ]),

        spacer,
        # Metric display
        html.Div(className="row", children=[
            html.Div(className="col col-2", children=[
                sd_material_ui.Paper(
                    className="flex between", children=[
                        html.Div(className="body2", children="Metric"),
                        html.Div(className="body2", children=123)
                    ])
            ]),
        ]),

        spacer,

        # Date picker
        html.Div(className="row", children=[
            html.Div(className="col col-4", children=[
                sd_material_ui.Paper(children=[
                    sd_material_ui.Picker(
                        id="date-picker-1", label="Date Picker", type="date"),
                    sd_material_ui.Picker(
                        id="date-picker-2", label="Time Picker", type="time"),
                    sd_material_ui.Picker(
                        id="date-picker-3", label="Date Dialog", type="date-dialog")
                ])
            ]),
        ]),

        spacer,

        # Text Input
        html.Div(className="row", children=[
            html.Div(className="col col-4", children=[
                sd_material_ui.Paper(children=[
                    sd_material_ui.TextField(id="textfield-1")
                ])
            ])
        ]),

        spacer

    ]),
    sidebar
])

# app.layout = html.Div(children=[

#     sd_material_ui.Paper(children=[
#     html.Div(className="row", children=[

#         html.Div(className="col", children=[
#             sd_material_ui.Subheader(['Sample Graph']),
#             html.Div([
#                 dcc.Graph(id='graph-with-slider'),
#             ]),
#         ]),

#         html.Div(className="col", children=[
#             sd_material_ui.Button(children='Test',
#                 id='button1',
#                 disableShadow=False,
#                 useIcon=False,
#                 variant='contained',
#                 color="primary",),

#             spacer,

#             html.Div(children=[
#                 sd_material_ui.DropDownMenu(
#                         id='dropdown-input',
#                         labelText='Test',
#                         labelId='dropdown-label',
#                         value=1,
#                         useGrouping=True,
#                         variant="outlined",
#                         options=[
#                             dict(grouping='Group A'),
#                             dict(primaryText='Option 1', value=1),
#                             dict(primaryText='Option 2', value=2),
#                             dict(grouping='Group B'),
#                             dict(primaryText='Option 3', value=3),
#                             dict(grouping='Group C'),
#                             dict(primaryText='Option 4', value=4),
#                         ])
#                     ],
#                 style={'width': 200}),

#             html.P(id='dropdown-output', style={"fontFamily": "Amaranth", "fontWeight": "normal"}),

#             spacer,

#             sd_material_ui.Slider(
#                 id='test-slider',
#                 valueLabelDisplay="auto",
#                 min=df['year'].min(),
#                 max=df['year'].max(),
#                 value=df['year'].min(),
#                 marks=[{'value': year, 'label': str(year)} for year in df['year'].unique()],
#             ),

#             spacer,

#             sd_material_ui.ColorPicker(id='colorpicker-input'),
#             html.Div(id="colorpicker-output")
#     ]),
# ])]),

#     spacer,

#     html.Div(className="row", children=[
#         sd_material_ui.Paper(className="col", children=[
#             html.Div(children=[
#                 dcc.Graph(id='graph-with-slider-2'),
#             ]),
#         ]),
#         sd_material_ui.Paper(className="col", children=[
#         html.Div(children=[
#             dcc.Graph(id='graph-with-slider-3'),
#         ]),]),
#     ]),

# ])


# @app.callback(
#     Output('graph-with-slider', 'figure'),
#     Input('test-slider', 'value'))
# def update_figure(selected_year):
#     print(selected_year)

#     filtered_df = df[df.year == int(selected_year)]

#     # print(filtered_df.year.dtypes, type(selected_year))

#     fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
#                      size="pop", hover_name="country",
#                      log_x=True, size_max=55)

#     fig.update_layout(transition_duration=500)

#     return fig


# @app.callback(
#     dash.dependencies.Output('dropdown-output', 'children'),
#     [dash.dependencies.Input('dropdown-input', 'value')])
# def dropdown_callback(value):
#     return ['Selection is: {}'.format(value)]


# @app.callback(
#     Output('colorpicker-output', 'children'),
#     Input('colorpicker-input', 'value')
# )
# def colorpicker_callback(value):
#     return value


if __name__ == '__main__':
    app.run_server(debug=True)
