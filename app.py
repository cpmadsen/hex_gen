from pathlib import Path
import numpy as np
## import plotly.graph_objs as go
# To install the 'shiny' module, use 'pip install https://github.com/posit-dev/py-shiny/tarball/main'
from shiny import App, reactive, ui
from htmltools import css, HTML, div


# Once a shiny app is being rendered in the simple browser,
# every time you save the script, the rendered app while automatically refresh.

## from shinywidgets import output_widget, register_widget
## from sklearn.linear_model import LinearRegression

mats_path = Path(__file__).parent / "www"

app_ui = ui.page_fluid(
    ui.include_css("styles.css"),
    ui.tags.style(
        """
        .sidebar {
            background: url(stone_wall_2.png);
            border: 10px solid transparent;
            padding: 5px;
            border-image: url(wood_frame_crop.png) 75 round;
            border-image-width: 10px;
            }
            
        @font-face {  
            src: url(ENDOR.ttf);
            font-family: "Endor";
            }

            .endor {
                font-family: 'Endor';
            }
        """),
    ui.tags.script("page_load_extras.js"),
    ui.tags.script("document.getElementById('w2_music').play()"),
    #div(
        HTML('<audio id="w2_music" src = "https://vgmsite.com/soundtracks/warcraft-2-tides-of-darkness-cda/ljjizkibrg/02%20-%20Human%20Battle%2001.mp3?raw=true"></audio>'),
        HTML("<script>document.getElementById('w2_music').play()</script>"),
    #    ),
    ui.layout_sidebar(
        sidebar = ui.panel_sidebar(
            ui.div(ui.tags.h3('HexGen',{"class": "centered_text over-background endor"}), 
                {"class": "box"}),
            ui.input_text("txt", "Project Name:", "My_map_1"),
            ui.input_slider("slider", "Number of Hexes (horizontal):", 1, 100, 30),
            ui.input_slider("slider", "Number of Hexes (vertical):", 1, 100, 30),
            ui.input_action_button("action", "Create Hex Map"),
            ui.tags.h5("actionButton with CSS class:"),
            ui.input_action_button(
                "action2", "Action button", class_="btn-primary"
            ),
            width=4,
            class_= 'ui-with-bg'
        ),
        main = ui.panel_main(
            ui.navset_tab(
                ui.nav("Tab 1"),                
                ui.nav("Tab 2"),
                ui.nav("Tab 3")
            )
        )
    )
)


def server(input, output, session):
    1 + 1

www_dir = Path(__file__).parent / "www"
app = App(app_ui, server, static_assets=www_dir)