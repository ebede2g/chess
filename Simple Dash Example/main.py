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
            cell = html.Button(id=f"{i}_{j}",
                               style={'backgroundColor': color, 'width': '50px', 'height': '50px'})
            row.append(cell)
        chessboard.append(html.Div(row, className='chess-row'))
    return chessboard


app.layout = html.Div(
    [
        html.H1("Шахматна дошка"),
        html.Div(create_chessboard(), className='chessboard'),
        html.Plaintext(id="move_history")
    ]
)


# @app.callback(Output("move_history", "children"), [Input(f"{i}-{j}", "n_clicks") for i in range(8) for j in range(8)] )
# def record_move(*args):
#     ctx = dash.callback_context
#     if not ctx.triggered:
#         return ""
#
#     cell_id = ctx.triggered[0]["prop_id"].split(".")[0]
#     row, col = map(int, cell_id.split("-"))
#
#     with open("moves.txt", "a") as f:
#         f.write(f"({row}, {col}) - {datetime.datetime.now()}\n")
#
#     return "Move recorded successfully!"


if __name__ == '__main__':
    app.run_server(debug=True)
