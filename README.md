# test-reflex

Testing reflex - gradio integration 

1. Using Pyodide 
2. Embedding a HF space (or equivalently a local deployment) with iframe 
3. Embedding a HF space with web components.
 
You can use `rye sync` to create a local virtual environment followed by `reflex run` to run the app.

The following routes can then be tested. 
```python
app.add_page(index, route="/")
app.add_page(gradio_lite, route="/gradio_lite")
app.add_page(gradio_embed_iframe, route="/gradio_embed_iframe")
app.add_page(gradio_embed_webcomponent, route="/gradio_embed_webcomponent")
```

