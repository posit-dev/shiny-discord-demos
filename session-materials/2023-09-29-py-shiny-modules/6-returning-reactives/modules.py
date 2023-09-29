import pandas as pd
from shiny import App, Inputs, Outputs, Session, module, reactive, render, req, ui


@module.ui
def city_state_ui():
    return ui.TagList(
        ui.input_selectize(
            "state", "State", choices=["NY", "CO", "OR", "MI"], selected="NY"
        ),
        ui.output_ui("cities_ui"),
    )


@module.server
def city_state_server(input: Inputs, output: Outputs, session: Session):
    data = {
        "state": ["NY", "CO", "OR", "MI"] * 5,
        "city": [
            "New York",
            "Denver",
            "Portland",
            "Detroit",
            "Buffalo",
            "Colorado Springs",
            "Salem",
            "Grand Rapids",
            "Rochester",
            "Aurora",
            "Eugene",
            "Warren",
            "Yonkers",
            "Lakewood",
            "Gresham",
            "Sterling Heights",
            "Syracuse",
            "Fort Collins",
            "Hillsboro",
            "Ann Arbor",
        ],
    }
    df = pd.DataFrame(data)

    @output
    @render.ui
    def cities_ui():
        opts = df[df["state"] == input.state()]["city"].unique().tolist()
        return ui.input_selectize("cities", "Cities", choices=opts, selected=opts[0])

    return input.cities, input.state
