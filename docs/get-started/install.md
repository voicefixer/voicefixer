# Installation

You can install VoiceFixer from PyPI or directly from the source repository.

::::{tab-set}

:::{tab-item} PyPI
Here's how to install the latest stable release of VoiceFixer 2 from PyPI:
```bash
pip install -U voicefixer2
```
:::

:::{tab-item} Direct Installation
Here's how to install the latest development release of VoiceFixer 2 from PyPI:
```bash
pip install -U git+https://github.com/voicefixer/voicefixer
```
:::

::::


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
```bash
sudo apt install ffmpeg
```
:::

:::{tab-item} Windows
```bash
scoop install ffmpeg
```
:::

::::

Please see [FFmpeg's website](https://ffmpeg.org/) for more installation details.