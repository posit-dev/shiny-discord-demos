from shiny import App, ui, reactive
from modules import multiply_ui, multiply_server


app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.input_numeric("multiplier", "Global multiplier", 10),
            ui.input_action_button("reset", "Reset all values"),
        ),
        ui.panel_main(
            multiply_ui("multiply1"),
            multiply_ui("multiply2"),
        ),
    )
)


def server(input, output, session):
    multiply_server("multiply1", multiplier=input.multiplier, reset_button=input.reset)
    multiply_server("multiply2", multiplier=input.multiplier, reset_button=input.reset)

    @reactive.Effect
    @reactive.event(input.reset)
    def reset_numerics():
        ui.update_numeric("multiplier", value=10)


app = App(app_ui, server)
