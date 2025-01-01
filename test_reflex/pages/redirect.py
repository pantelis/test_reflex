import reflex as rx

def gradio_redirect() -> rx.Component:
    return rx.center(
        rx.button(
            "Open Gradio App in New Tab",
            on_click=rx.redirect(
                "http://localhost:8002/gradio_redirect",
                is_external=True,
            ),
        ),
        width="100vw",  # Full viewport width
        height="100vh",  # Full viewport height
        justify="center",
    )



    
        
    