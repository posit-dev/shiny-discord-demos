from shiny import module, ui, render, reactive, event


@module.ui
def multiply_ui():
    return ui.div(
        {"style": "border: 1px solid #ccc; border-radius: 5px; margin: 5px 0;"},
        ui.input_numeric("base_number", "Number to multiply", 5),
        ui.output_text("text_out"),
    )


@module.server
def multiply_server(input, output, session, multiplier, reset_button):
    @output
    @render.text
    def text_out():
        return f"{input.base_number()} * {multiplier()} = {input.base_number() * multiplier()}"

    @reactive.Effect
    @reactive.event(reset_button)
    def reset_numerics():
        ui.update_numeric("base_number", value=5)
