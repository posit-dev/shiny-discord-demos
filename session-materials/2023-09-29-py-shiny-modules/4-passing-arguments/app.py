from shiny import App, ui
from modules import counter_ui, counter_server


app_ui = ui.page_fluid(
    counter_ui("counter1", label="Counter 1"),
    counter_ui("counter2", label="Counter 2"),
)


def server(input, output, session):
    counter_server("counter1")
    counter_server("counter2")


app = App(app_ui, server)
