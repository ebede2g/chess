import datetime
from dash import Dash, dash_table, dcc, html
from dash.dependencies import Input, Output, State
from plotly.graph_objs import Scatter, Bar






app = Dash(title='Simple Dash Example', prevent_initial_callbacks=True, serve_locally=True)
app.layout = html.Div([

    html.Div([
        html.H2('Here is a sample of server button:'),
        html.Button("Test button 1 (click to get current time from server)", id="test_btn_1", style={'display': 'inline-block'}),
        html.Plaintext('Current server time:', id="B_GetServerTime", style={'display': 'inline-block'})
    ]),


],
style={'width': '500'},
)


@app.callback(Output("B_GetServerTime", "children"), Input("test_btn_1", "n_clicks"))
def get_cur_svr_time(n_clicks):
    return "ss "+format(datetime.datetime.today())



if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1', port='6615')