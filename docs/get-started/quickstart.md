# Quick Start

Here are some basic examples. Check out the Usage section for more detailed documentation.

## CLI

Restore a single file:

```bash
voicefixer file input.wav output.wav
```

Restore all `.mp3` or `.wav` files in a directory:

```bash
voicefixer folder input_folder output_folder
```

## Python API

Run all modes:

```python
from voicefixer import VoiceFixer
voicefixer = VoiceFixer()
for mode in [0, 1, 2]:
    print("Running mode", mode)
    voicefixer.restore(
        input='test.wav',
        output="output_" + str(mode) + ".wav",
        cuda=True,
        mode=mode
    )
```