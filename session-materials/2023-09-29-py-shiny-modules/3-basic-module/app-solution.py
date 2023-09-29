from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui, module
from modules import io_row_ui, io_row_server

app_ui = ui.page_fluid(
    io_row_ui("first_row"),
    io_row_ui("second_row"),
)


def server(input: Inputs, output: Outputs, session: Session):
    io_row_server("first_row")
    io_row_server("second_row")


app = App(app_ui, server)
