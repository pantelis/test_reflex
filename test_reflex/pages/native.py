import gradio as gr


def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)


def gradio_native() -> gr.Interface:
    return gr.Interface(
        fn=greet,
        inputs=["text", "slider"],
        outputs=["text"],
    )

gradio_native = gradio_native()

#gradio_native.launch(share=True, debug=True, server_port=7860)

