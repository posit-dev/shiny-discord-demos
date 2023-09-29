from shiny import App, ui


def my_slider(id):
    return ui.input_slider(id, "N", 0, 100, 20)


app_ui = ui.page_fluid(
    my_slider("n1"),
    my_slider("n2"),
)

app = App(app_ui, None)
