from shiny import module, ui, render, reactive, event


@module.ui
def counter_ui(label="Counter"):
    return ui.div(
        {"style": "border: 1px solid #ccc; border-radius: 5px; margin: 5px 0;"},
        ui.h2("This is " + label),
        ui.input_action_button(id="button", label=label),
        ui.output_text_verbatim(id="out"),
    )


@module.server
def counter_server(input, output, session):
    count = reactive.Value(0)

    @reactive.Effect
    @reactive.event(input.button)
    def _():
        count.set(count() + 1)

    @output
    @render.text
    def out():
        return f"Click count is {count()}"
