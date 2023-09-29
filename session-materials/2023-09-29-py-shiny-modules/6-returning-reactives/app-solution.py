from shiny import App, ui, render
from modules import city_state_ui, city_state_server


app_ui = ui.page_fluid(city_state_ui("city_selector"), ui.output_text("selected"))


def server(input, output, session):
    cities, state = city_state_server("city_selector")

    @output
    @render.text
    def selected():
        return f"You selected '{cities()}' in '{state()}'"


app = App(app_ui, server)
