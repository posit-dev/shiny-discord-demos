from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui, module


@module.ui
def io_row_ui():
    return ui.row(
        ui.column(6, ui.input_text("text_input", "Enter text")),
        ui.column(6, ui.output_text("text_output")),
    )


@module.server
def io_row_server(input: Inputs, output: Outputs, session: Session):
    @output
    @render.text
    def text_output():
        return f"You entered '{input.text_input()}'"


app_ui = ui.page_fluid(
    io_row_ui("first_row"),
    io_row_ui("second_row"),
)


def server(input: Inputs, output: Outputs, session: Session):
    io_row_server("first_row")
    io_row_server("second_row")


app = App(app_ui, server)
