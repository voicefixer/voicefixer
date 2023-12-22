# Quick Start

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
