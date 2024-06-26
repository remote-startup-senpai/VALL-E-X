# VALL-E X: Multilingual Text-to-Speech Synthesis and Voice Cloning 🔊

A quicker setup for the open source implementation of Microsoft's [VALL-E X](https://arxiv.org/pdf/2303.03926) zero-shot TTS model by [Plachtaa](https://github.com/Plachtaa).

More details about the model in the [thorough README](README-EN-long.md).

### Requirements

- `python`

### Setup

1. Install the requirements

```
pip install -r requirements.txt
```

2. (Optional) This is run automatically when you execute for the first time. However, if you'd like to setup the models, simply run [`./init_models.sh`](init_models.sh) to download the required model checkpoints

### Execution

You can use either of the following:
  - the Gradio demo by running `python launch-ui.py` and using the app on http://localhost:7860 (opens automatically)
  - the code version in [`start.ipynb`](start.ipynb)
