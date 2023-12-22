# Installation

You can install VoiceFixer from PyPI or directly from the source repository.


:::::{tab-set}

::::{tab-item} PyPI
:::{warning}
When installing from PyPI, make sure you install `voicefixer2` and not `voicefixer`. Installing `voicefixer` will install the original version of VoiceFixer, which may be incompatible with VoiceFixer 2.
:::
Here's how to install the latest stable release of VoiceFixer 2 from PyPI:
```bash
pip install -U voicefixer2
```
::::

::::{tab-item} Direct Installation
Here's how to install the latest development release of VoiceFixer 2 from PyPI:
```bash
pip install -U git+https://github.com/voicefixer/voicefixer
```
::::

:::::

:::::{note}
If you have any issues on Apple Silicon, please install PyTorch Nightly:

::::{tab-set}

:::{tab-item} PyPI
Install PyTorch Nightly from PyPI.
```bash
pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cpu
```
:::

:::{tab-item} Conda
Install PyTorch Nightly from Conda.
```bash
conda install pytorch-nightly::pytorch torchvision torchaudio -c pytorch-nightly
```
:::

::::

:::::

## Including in Requirements

You may include voicefixer2 in your requirements.txt file:

```
voicefixer2
```

or

```
git+https://github.com/voicefixer/voicefixer
```

or, in setup.py

```python
[
    'voicefixer2 @ git+https://github.com/voicefixer/voicefixer',
]
```

or simply

```python
[
    'voicefixer2',
]
```

## FFmpeg

For non-WAV support (MP3/OGG/etc), you must install [FFmpeg](https://ffmpeg.org/).

::::{tab-set}

:::{tab-item} macOS
Here's how to install FFmpeg on macOS:
```bash
brew install ffmpeg
```
:::

:::{tab-item} Linux/Ubuntu
Here's how to install FFmpeg on Linux/Ubuntu:
```bash
sudo apt install ffmpeg
```
:::

:::{tab-item} Windows
Here's how to install FFmpeg on Windows:
```bash
scoop install ffmpeg
```
:::

::::

Please see [FFmpeg's website](https://ffmpeg.org/) for more installation details.