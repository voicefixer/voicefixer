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

## Loading with Librosa

```python
# Import modules
from voicefixer import VoiceFixer
import torch
import librosa
import soundfile as sf
# Initialize VF
voicefixer = VoiceFixer()
# Check if GPU is available
gpu_available = torch.cuda.is_available() or torch.backends.mps.is_available()
# Load audio
wav, _ = librosa.load('test.wav', sr=22050) # Only works on .wav
# Restore audio in mode 0
out = voicefixer.restore_inmem(wav, gpu_available, 0)
# Save audio
shape = list(frames.shape)
if len(shape) == 1:
    frames = frames[..., None]
in_samples, in_channels = shape[-2], shape[-1]
if in_channels >= 3:
    if len(shape) == 2:
        frames = np.transpose(frames, (1, 0))
    elif len(shape) == 3:
        frames = np.transpose(frames, (0, 2, 1))
if (np.max(frames) <= 1 and frames.dtype == np.float32 or frames.dtype == np.float16 or frames.dtype == np.float64):
    frames *= 2 ** 15
frames = frames.astype(np.short)
if len(frames.shape) >= 3:
    frames = frames[0, ...]
# Write to file
sf.write('output.wav', frames, samplerate=sample_rate)
```