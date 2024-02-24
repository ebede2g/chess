import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import datetime
lib = 'lib/'

newChessBoard = [
    ['0т', '0к', '0т', '0ф', '0К', '0т', '0к', '0т'],
    ['0п', '0п', '0п', '0п', '0п', '0п', '0п', '0п'],
    ['__', '__', '__', '__', '__', '__', '__', '__'],
    ['__', '__', '__', '__', '__', '__', '__', '__'],
    ['__', '__', '__', '__', '__', '__', '__', '__'],
    ['__', '__', '__', '__', '__', '__', '__', '__'],
    ['1п', '1п', '1п', '1п', '1п', '1п', '1п', '1п'],
    ['1т', '1к', '1т', '1ф', '1К', '1т', '1к', '1т'],
]
with open(f'{lib}current_board.txt', "w") as f:
    pass
with open(f'{lib}current_board.txt', "a") as f:
    for i in range(8):
        for j in range(8):
            f.write(newChessBoard[i][j]+" ")
        f.write("\n")
# chess = open(f'{lib}current_board.txt').read().splitlines()



app = dash.Dash(title='Simple Dash Example', prevent_initial_callbacks=True, serve_locally=True)

# Створення шахматної дошки
def createNewChessboard():
    chessboard = []
    for i in range(8):
        row = []
        for j in range(8):
            color = "white" if (i + j) % 2 == 0 else "black"
            cell = html.Button(
                id=f"{i}_{j}",
                style={'backgroundColor': color,
                       'width': '50px',
                       'height': '50px',
                       'color': 'red',
                       'font-size': '8px'
                       },
                children=f'__'
            )
            row.append(cell)
        chessboard.append(html.Div(row, className='chess-row'))
    return chessboard

app.layout = html.Div(
    [
        html.H1("Шахматна дошка"),
        html.Div(createNewChessboard(), className='chessboard'),
        html.Plaintext('Запсиувач ходів [пусто]', id="move_history")
    ]
)



for i in range(8):
    for j in range(8):
        @app.callback(
            Output("move_history", "children", allow_duplicate=1),
            Output(f"{i}_{j}", "children"),
            Input(f"{i}_{j}", "n_clicks"),

        )
        def record_move(n_clicks, row=i, col=j):
            with open(f"{lib}moves.txt", "a") as f:
                f.write(f"({row}, {col}) - {datetime.datetime.now()}\n")

            return "Move recorded successfully!", "тик"

if __name__ == '__main__':
    app.run_server(debug=True, port='5912')
