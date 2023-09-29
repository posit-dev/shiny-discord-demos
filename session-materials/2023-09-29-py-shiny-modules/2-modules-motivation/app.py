from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui


def io_row(prefix):
    return ui.row(
        ui.column(6, ui.input_text(f"{prefix}_text_input", "Enter text")),
        ui.column(6, ui.output_text(f"{prefix}_text_output")),
    )


app_ui = ui.page_fluid(
    io_row("first_row"),
    io_row("second_row"),
)


def server(input: Inputs, output: Outputs, session: Session):
    @output
    @render.text
    def first_row_text_output():
        return f"You entered '{input.first_row_text_input()}'"

    @output
    @render.text
    def second_row_text_output():
        return f"You entered '{input.second_row_text_input()}'"


app = App(app_ui, server)
