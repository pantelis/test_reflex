import reflex as rx


# iframe method
def docs() -> rx.Component:
    return rx.box(
        rx.html(
            """
            <iframe 
                src="http://localhost:7511" 
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
