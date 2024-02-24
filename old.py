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



###################


import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import datetime

app = dash.Dash(title='Simple Dash Example', prevent_initial_callbacks=True, serve_locally=True)

# Створення шахматної дошки
def create_chessboard():
    chessboard = []
    for i in range(8):
        row = []
        for j in range(8):
            color = "white" if (i + j) % 2 == 0 else "black"
            cell = html.Button(
                id=f"{i}_{j}",
                style={'backgroundColor': color, 'width': '50px', 'height': '50px'});
            row.append(cell)
        chessboard.append(html.Div(row, className='chess-row'))
    return chessboard


app.layout = html.Div(
    [
        html.H1("Шахматна дошка"),
        html.Div(create_chessboard(), className='chessboard'),
        html.Plaintext('Запсиувач ходів [пусто]',id="move_history")
    ]
)

for i in range(8):
    for j in range(8):
        @app.callback(Output("move_history", "children"), [Input(f"{i}_{j}", "n_clicks")])
        def record_move(*args):
            ctx = dash.callback_context
            if not ctx.triggered:
                return ""

            cell_id = ctx.triggered[0]["prop_id"].split(".")[0]
            row, col = map(int, cell_id.split("-"))

            with open("moves.txt", "a") as f:
                f.write(f"({row}, {col}) - {datetime.datetime.now()}\n")

            return "Move recorded successfully!"


if __name__ == '__main__':
    app.run_server(debug=True)
