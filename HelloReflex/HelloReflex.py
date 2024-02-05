"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1


def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
            rx.heading("Prueba de Reflex!", font_size="2em"),
            rx.text("Hola Mundo", 
                    color=["orange", "red", "purple", "blue", "green"]),   # Cambia de color el texto según el tamaño de la pantalla.
                    
            
            rx.text("Idiomas", 
                    color=["orange", "red", "purple", "black", "green"]), 
            rx.card(
                rx.text("Body 1"),
                        header=rx.heading("Header 1", size="lg"),
                        footer=rx.heading("Footer 1", size="sm"),
                ),
            rx.text("Experiencia Laboral", 
                    color=["orange", "red", "purple", "black", "green"]), 
            rx.card(
                rx.text("Body 2"),
                        header=rx.heading("Header 2", size="lg"),
                        footer=rx.heading("Footer 2", size="sm"),
            ),

            rx.link(
                "About Link",
                href="/about",
            ),
            rx.link(
                "Check out our docs!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": rx.color_mode_cond(
                        light="rgb(107,99,246)",
                        dark="rgb(179, 175, 255)",
                    )
                },
                spacing="0.5em",
                font_size="2em",
                #padding_top="5%",
            ),
        ),
    )

def about() -> rx.Component:
    return rx.fragment(
        rx.text("Pagina About", 
                color="blue"), 
                
        rx.link(
                "Principal",
                href="/",
            ),
    )


# Create app instance and add index page.
app = rx.App()
app.add_page(index, route="/")
app.add_page(about, route="/about")
