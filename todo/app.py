import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.H1("To-Do List"),
    dbc.Input(id='task-input', placeholder='Enter task...', type='text', className="mb-2"),
    dbc.Button("Add Task", id='add-task', color="primary", className="mb-2"),
    html.Ul(id='task-list', className="list-group"),
])

@app.callback(
    Output('task-list', 'children'),
    [Input('add-task', 'n_clicks')],
    [State('task-input', 'value'),
     State('task-list', 'children')]
)
def add_task(n_clicks, task, current_tasks):
    if n_clicks is None:
        return current_tasks
    if current_tasks is None:
        current_tasks = []
    if task:
        current_tasks.append(html.Li(task, className="list-group-item"))
    return current_tasks

if __name__ == '__main__':
    app.run_server(debug=True)
