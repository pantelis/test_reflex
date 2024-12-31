import reflex as rx

def gradio_lite() -> rx.Component:
    return rx.vstack(
        rx.script(
            """
            <gradio-lite>
            import gradio as gr

            def greet(name):
                return "Hello, " + name + "!"

            gr.Interface(greet, "textbox", "textbox").launch()
            </gradio-lite>
            """
        ),
    )
