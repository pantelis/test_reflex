"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import gradio as gr
from fastapi import FastAPI, Request, Response
import httpx
from rxconfig import config
from .pages.lite import gradio_lite
from .pages.native import gradio_native
from .pages.embed import gradio_embed_iframe, gradio_embed_webcomponent
from .pages.docs import docs
from .pages.redirect import gradio_redirect
import subprocess


class State(rx.State):
    """The app state."""
    pass



# TODO: Update the Next.js config before running the Reflex app to allow the quarto static site generator to work without iframe
# def update_next_config():
#     subprocess.run(["python", "update_next_config.py"], check=True)

# # Update Next.js config before running the Reflex app
# update_next_config()


app = rx.App(
    head_components=[
        rx.html('<script type="module" crossorigin src="https://cdn.jsdelivr.net/npm/@gradio/lite/dist/lite.js"></script>' +
		        '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@gradio/lite/dist/lite.css" />'),
        # rx.script(src="https://cdn.jsdelivr.net/npm/@gradio/lite/dist/lite.js"),
        rx.script(src="https://gradio.s3.us-west-2.amazonaws.com/3.12.0/gradio.js"),
    ]
)


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                on_click=rx.redirect("/docsite"
                ),
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app.add_page(index, route="/")
app.add_page(gradio_lite, route="/gradio_lite")
app.add_page(gradio_embed_iframe, route="/gradio_embed_iframe")
app.add_page(gradio_embed_webcomponent, route="/gradio_embed_webcomponent")
app.add_page(gradio_redirect, route="/gradio_redirect")
app.add_page(docs, route="/docs")

# The following code is for the FastAPI redirect - see README.md for more details
CUSTOM_PATH = "/gradio_redirect"

reflex_fastapi = app.api
reflex_fastapi = gr.mount_gradio_app(
    reflex_fastapi, gradio_native, path=CUSTOM_PATH, server_port=8002
)


# from fastapi.staticfiles import StaticFiles
# app.api.mount("/docs", StaticFiles(directory="docs/_manuscript/", html=True), name="docs")

# from fastapi.responses import HTMLResponse

# async def serve_docs():
#     with open("docs/_manuscript/index.html") as f:
#         content = f.read()
#     return HTMLResponse(content)

# app.api.add_api_route("/documents", serve_docs)