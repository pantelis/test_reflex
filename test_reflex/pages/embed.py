import reflex as rx

# iframe method
def gradio_embed_iframe() -> rx.Component:
    return rx.box(
        rx.html(
            """
            <iframe 
                src="https://pantelism-test.hf.space" 
                style="width: 100%; height: 100vh; border: none;" 
                allowfullscreen 
                loading="lazy">
            </iframe>
            """
        ),
        width="100%",
        height="100vh",
        padding="0",
        margin="0",
    )


def gradio_embed_webcomponent() -> rx.Component:
    return rx.box(
        rx.html(
            """<gradio-app src="https://pantelism-test.hf.space"></gradio-app>"""
        )
    )