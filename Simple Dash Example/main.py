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
            f.write(newChessBoard[i][j] + " ")
        f.write("\n")

app = dash.Dash(title='Simple Dash Example',prevent_initial_callbacks=True)



def updateChessboard():
    chessboard = []
    with open(f'{lib}current_board.txt', 'r') as file:
        curBoardReadRow = file.readlines()

        for i in range(8):
            row = []
            for j in range(8):
                color = "white" if (i + j) % 2 == 0 else "black"
                cell = html.Table(
                    id=f"{i}//{j}",
                    style={'backgroundColor': color,
                           'width': '40px',
                           'height': '40px',
                           'color': 'red',
                           'font-size': '8px',
                           },
                    children=f'{curBoardReadRow[i][3 * j:3 * j + 2]}'
                )
                row.append(cell)
            chessboard.append(html.Div(row, className='chess-row',style={'display': 'inline-block'}))
        return chessboard




app.layout = html.Div(
    [
        html.H1("Шахматна дошка"),
        html.Div(id="chessboard", children=updateChessboard(), className='chessboard'),
        html.Plaintext('Записувач ходів [деактивований]', id="move_history"),

        dcc.Interval(id='tick', disabled=True, n_intervals=0)
    ]
)



@app.callback(
    Output('chessboard', 'children',allow_duplicate=True),
    Input('tick', 'n_intervals')
)
def update_chessboard(n_intervals):
    print(f"Live upd {n_intervals}")
    return updateChessboard()


@app.callback(
    Output("move_history", "children",),
    Output("chessboard", "children"),
    Output('tick','n_intervals'),
    Input("chessboard", "n_clicks"),
)
def record_move(n_clicks):
    return f"Move recorded successfully!", updateChessboard() , 1



# @app.callback(
#     Output("move_history", "children"),
#     Output('chessboard', 'children'),
#     Input("00", "n_clicks"),
# )
# def record_move(n_clicks):
#    return "Move recorded successfully!", updateChessboard()




if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port='2133')
