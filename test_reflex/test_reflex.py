"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import gradio as gr
from fastapi import FastAPI, Request, Response
import httpx
from rxconfig import config
from .pages.lite import gradio_lite
from .pages.native import gradio_native
from .pages.embed import gradio_embed_iframe, gradio_embed_webcomponent

class State(rx.State):
    """The app state."""

    ...


app = rx.App(
    head_components=[
        rx.html('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@gradio/lite/dist/lite.css" />'),
       rx.script(src="https://cdn.jsdelivr.net/npm/@gradio/lite/dist/lite.js"),
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
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app.add_page(index, route="/")
app.add_page(gradio_lite, route="/gradio_lite")
#app.add_page(gradio_native, route="/gradio_native")
app.add_page(gradio_embed_iframe, route="/gradio_embed_iframe")
app.add_page(gradio_embed_webcomponent, route="/gradio_embed_webcomponent")

# Define Gradio interface
#io = gr.Interface(lambda x: "Hello, " + x + "!", "textbox", "textbox")

# # Mount Gradio app onto Reflex's underlying FastAPI app
# fastapi_app = FastAPI()  # Access Reflex's underlying FastAPI app



# # Add CORS middleware to allow WebSocket connections from Reflex frontend
# app.api.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3001", "http://127.0.0.1:3001"],  # Frontend URLs
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# Define the proxy route for /grad
# @app.api.api_route("/grad/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
# async def proxy_grad(request: Request, path: str):
#     """
#     Proxy requests to /grad to localhost:8001/grad.
#     """
    
#     app.api = gr.mount_gradio_app(app.api, io, path="/grad")

#     target_url = f"http://localhost:8001/grad/{path}"

#     # Create an async client for forwarding requests
#     async with httpx.AsyncClient() as client:
#         # Forward the request to the target URL
#         response = await client.request(
#             method=request.method,
#             url=target_url,
#             headers={
#                 key: value for key, value in request.headers.items() if key != "host"
#             },
#             content=await request.body(),
#             params=request.query_params,
#         )

#     # Create a FastAPI Response object with the proxied response
#     return Response(
#         content=response.content,
#         status_code=response.status_code,
#         headers=dict(response.headers),
#     )


# # Define a simple route for /
# @app.get("/")
# async def root():
#     return {"message": "Welcome to the main application!"}

#app._compile()
# Run this with `uvicorn` to test:
# uvicorn app:app --reload --port 3001
