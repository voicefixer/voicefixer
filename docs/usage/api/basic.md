# Basic Usage

Here are some examples of usage of the VoiceFixer Python API. Please see the Advanced Usage section for details about modes.

## Restore a File

```python
# Import modules
from voicefixer import VoiceFixer
import torch
# Initialize VF
voicefixer = VoiceFixer()
# Check if GPU is available
gpu_available = torch.cuda.is_available() or torch.backends.mps.is_available()
# Restore a file in mode 0
voicefixer.restore(
    input='input.wav', output='output.wav', cuda=gpu_available, mode=0
)
```