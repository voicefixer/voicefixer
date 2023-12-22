# Installation

You can install VoiceFixer from PyPI or directly from the source repository.

::::{note}
When installing from PyPI, make sure you install `voicefixer2` and not `voicefixer`. Installing `voicefixer` will install the original version of VoiceFixer, which may be incompatible with VoiceFixer 2.
::::

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