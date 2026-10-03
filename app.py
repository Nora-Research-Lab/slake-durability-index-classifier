import gradio as gr
from slake_durability_index_classifier import (
    classify_sdi,
    plot_sdi_classification,
    typical_rock_types,
)

def classify_interface(id2, id1):
    try:
        id2 = float(id2)
    except (TypeError, ValueError):
        return "Invalid input: Id2 must be a number.", None, ""
    if id2 < 0 or id2 > 100:
        return "Id2 must be between 0 and 100.", None, ""
    id1_val = None
    if id1 is not None and id1 != "":
        try:
            id1_val = float(id1)
            if id1_val < 0 or id1_val > 100:
                return "Id1 must be between 0 and 100.", None, ""
        except (TypeError, ValueError):
            return "Invalid input: Id1 must be a number.", None, ""
    classification, label = classify_sdi(id2, id1_val)
    fig = plot_sdi_classification(id2, id1_val)
    rocks = typical_rock_types(label)
    return classification, fig, rocks

with gr.Blocks(title="Slake Durability Index Classifier", css=".gradio-container {max-width: 800px; margin: auto;}") as demo:
    gr.Markdown(
        """
        # Slake Durability Index (SDI) Classifier
        Classify rock durability based on the second-cycle slake durability index (Id2).
        Optionally provide the first-cycle index (Id1) for a more refined classification.
        """
    )
    with gr.Row():
        with gr.Column():
            id2_input = gr.Number(
                label="Id2 (%)",
                minimum=0,
                maximum=100,
                step=0.1,
                value=90.0,
            )
            id1_input = gr.Number(
                label="Id1 (%) (optional)",
                minimum=0,
                maximum=100,
                step=0.1,
                value=None,
            )
            classify_btn = gr.Button("Classify")
        with gr.Column():
            output_text = gr.Textbox(label="Classification", lines=2)
            output_plot = gr.Plot(label="Durability Bar Chart")
            output_rocks = gr.HTML(label="Typical Rock Types")
    classify_btn.click(
        fn=classify_interface,
        inputs=[id2_input, id1_input],
        outputs=[output_text, output_plot, output_rocks],
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
