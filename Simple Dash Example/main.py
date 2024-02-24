import threading
import time

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


app = dash.Dash(title='Simple Dash Example', prevent_initial_callbacks=True, serve_locally=True)

# Створення шахматної дошки
def createNewChessboard():
    chessboard = []
    with open(f'{lib}current_board.txt', 'r') as file:
        curBoarReadRow = file.readlines()

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
                    children=f'{curBoarReadRow[i][3 * j:3 * j + 2]}'
                )
                row.append(cell)
            chessboard.append(html.Div(row, className='chess-row'))
        return chessboard


def my_loop():
    while True:
        app.layout = html.Div(
            [
                html.H1("Шахматна дошка"),
                html.Div(createNewChessboard(), className='chessboard'),
                html.Plaintext('Запсиувач ходів [пусто]', id="move_history")
            ]
        )
        time.sleep(1000)

loop_thread = threading.Thread(target=my_loop)
loop_thread.start()







for i in range(8):
    for j in range(8):
        @app.callback(
            Output("move_history", "children", allow_duplicate=1),
            Output(f"{i}_{j}", "children"),
            Input(f"{i}_{j}", "n_clicks"),

        )
        def record_move(n_clicks, row=i, col=j):
            with open("moves.txt", "a") as moves:
                moves.write(f"({row}, {col}) - {datetime.datetime.now()}\n")

            with open(f'{lib}current_board.txt', 'r') as file:
                curBoarReadRow = file.readlines()
                curBoarReadRow[row] = curBoarReadRow[row][:3 * col] + ":) " + curBoarReadRow[row][3 * col + 3:]
                with open(f'{lib}current_board.txt', 'w') as file:
                    file.writelines(curBoarReadRow)
                selected_chars = curBoarReadRow[row][3 * col:3 * col + 2]
                if(selected_chars==':) '):
                    selected_chars=':P'

            return "Move recorded successfully!", f"{selected_chars}"


if __name__ == '__main__':
    app.run_server(debug=True, port='1984')