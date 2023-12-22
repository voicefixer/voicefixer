<!-- [Website](https://voicefixer.github.io/) / [Live Demo](https://huggingface.co/spaces/voicefixer/voicefixer) / [Free API](https://huggingface.co/spaces/voicefixer/voicefixer-api) -->
<a href="https://voicefixer.github.io/"><img src="https://github.com/voicefixer/voicefixer/assets/76186054/8d9aeb00-1f7a-448d-b768-f984f3d22bc5" width="100"></a>
<a href="https://huggingface.co/spaces/voicefixer/voicefixer"><img src="https://github.com/voicefixer/voicefixer/assets/76186054/e81a773d-e0e6-43ad-878b-74013eb07e94" width="100"></a>
<a href="https://huggingface.co/spaces/voicefixer/voicefixer-api"><img src="https://github.com/voicefixer/voicefixer/assets/76186054/8d7c5932-9535-4ac9-9c04-72e2c123c0af" width="100"></a>

**Important:** The maintainers(s) of this repository are not affiliated or connected with the original version of VoiceFixer.

**Note:** We are actively accepting contributions (+ contributors)! Please check the To Do list for how you can contribute!

<img src="https://github.com/voicefixer/voicefixer/assets/76186054/4ff5a052-dbf2-4625-91fd-5f6739336a0f" width="500">

# <img src="https://camo.githubusercontent.com/a3b2d4da7e2d171fd691b5d2da5af46013dcb7904132485a3af7d14b6468aeac/68747470733a2f2f6769746875622d70726f64756374696f6e2d757365722d61737365742d3632313064662e73332e616d617a6f6e6177732e636f6d2f37363138363035342f3237303230343034382d34393962333538642d303036332d343562632d393235622d6434313336633035616633342e706e67" width="30"> VoiceFixer 2

Welcome to VoiceFixer 2, the next generation of VoiceFixer. VoiceFixer is a general speech restoration tool, using AI to remove background noise, fix degraded speech, enhance audio quality from old recordings, upscale audio resolution, and more, all in one model!

VoiceFixer aims to restore human speech, regardless of how seriously degraded it is. It can handle noise, reverberation, low resolution, and clipping effect within one model!

## What's different from the original VoiceFixer?

The [original version of VoiceFixer](https://github.com/haoheliu/voicefixer) continues to be updated with minor changes and bug fixes, however if one tries to install it and run it out of the box, one would encounter several errors that require modifying installed packages to fix.

**What’s the problem? How does this fix it?** VoiceFixer requires an old version of the `librosa` library, which is incompatible with new versions of the `numpy` library. We’ve fixed this issue by fixing the old version of `librosa` and `voicefixer`. We also added several new features.

### New features in VoiceFixer 2

We’ve added the following features in VoiceFixer 2:

* We’ve added MPS support, which means you can use GPU acceleration on M1 macs. You can enable this by setting the `cuda` parameter to `True`. It’s automatically enabled when using the command line interface (CLI).
* We've added a progress bar through TQDM for longer audio
* We now support non-WAV files (ie MP3)
* We're now using `cached_path` instead of hard-coding a cache path to increase OS support
* We're featuring faster model downloads w/ Hugging Face
* More features coming soon!

## Changelog

* Nov 18, 2023: Fix issue with model cache, thank to @gkarmas. Issue caused by spelling error 😳
* Nov 16, 2023: Upgrade librosa + torch
* Nov 11, 2023: Publish to PyPI
* Nov 11, 2023: Add progress bar support (requires `ffmpeg`) (see TODO below)
* Nov 11, 2023: Add preliminary MP3 support (requires `ffmpeg`) (see TODO below)
* Nov 11, 2023: Fix CLI issue (see TODO below)
* Sep 11, 2023: Forked from VoiceFixer

## To-Do

Here's what we still need to do - feel free to contribute:

- [ ] Fine-tune model for better results (this one requires $$$/compute :) - see [this](https://github.com/haoheliu/voicefixer_main) training repo)
- [ ] Add MP3 support for folders
- [ ] Allow user to restore an object (don't require a file)
- [ ] Allow user to input audio as an audio object, wave object, numpy array, torchaudio object, or pydub object and to output audio in varied formats as well, similar to how Gradio can accept audio in many different formats
- [ ] Update model to make [modifying state dict](https://github.com/voicefixer/voicefixer/commit/1b8c384bc2f34645e72c67e46db92b3accd20613) unnecessary - loading it twice increases VRAM usage (related to latest librosa issue)
    - [x] Update model
    - [ ] Remove code (still needs testing)
- [ ] [Realtime support](https://github.com/haoheliu/voicefixer_main/issues/11)
- [ ] [Add to HF Audio-to-Audio pipeline](https://huggingface.co/docs/hub/models-adding-libraries)
- [x] Support Windows (mostly file paths) - maybe use [cached_path](https://github.com/allenai/cached_path)
    - [ ] Fully test on Windows
- [ ] Clean up CLI (may have breaking changes)
- [x] Support custom models
- [x] Use latest version of librosa (probably pretty important, here's the issue the model doesn't work with latest torchlibrosa and the old torchlibrosa doesn't work with the latest librosa. need to completely retrain the model probably or change model python file) - fixed thanks to @manmay-nakhashi
- [x] Switch models from Zenodo to Hugging Face to increase speed and control over models (in progress)
- [x] Publish to pip (plz don't contribute on this one - I'll do it eventually but I have a certain workflow + system I like to use :) thanks!)
- [x] Add TQDM progress bar - crucial for longer conversions - maybe a beginner contribution?
- [x] Implement .mp3 support (currently only supports .wav) - probably won't be that hard - just need to use pydub. good beginner contribution!
- [x] Fix CLI instead of copying to /bin use CLI like [this](https://github.com/fakerybakery/simplesplit/blob/main/setup.py)

## Demo

[Check out the demos to see what VoiceFixer can do!](https://voicefixer.github.io/)

## Installation

**Don't want to install the package, but just want to try it out?**

Use our free API (no API key required) for audio files under 5 minutes. Non-commercial use only, audio may be collected. Details on [webpage](https://huggingface.co/spaces/voicefixer/voicefixer-api).

```bash
curl -X POST -H "Content-Type: multipart/form-data" -F "file=@test.mp3" https://voicefixer-voicefixer-api.hf.space/process_audio > processed_audio.wav
```

**NOTE: If you have any issues on Apple Silicon, please install PyTorch Nightly (`pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cpu`)**

You can install our package via. PyPI (Python Package Index), the official Python package index.

```
pip install voicefixer2
```

This will install the latest published release.

**If you would like to install the latest development version, or do not trust PyPI for any reason, please install directly from the source:**

```bash
pip install git+https://github.com/fakerybakery/voicefixer
```

### Including in Requirements

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

### FFmpeg

**NOTE:** For MP3/OGG/etc (non-WAV) support, you must install [FFmpeg](https://ffmpeg.org/)

**Quick Installation**

* macOS: `brew install ffmpeg`
* Linux/Ubuntu: `sudo apt install ffmpeg`
* Windows: `scoop install main/ffmpeg`

This is not guaranteed to work on all devices. Please see [FFmpeg's website](https://ffmpeg.org/) for instructions to install manually.

## Usage

**Important:** FFmpeg must be installed to support non-.wav files.

### Command Line

By default, if no output path is specified, the file will be saved to `outfile.wav`.

Process a file:

```bash
voicefixer --infile test/utterance/original/original.wav
```

Process all files in a directory:

```bash
voicefixer --infolder /path/to/input --outfolder /path/to/output
```

Change modes (default 0):

```bash
voicefixer --infile /path/to/input.wav --outfile /path/to/output.wav --mode 1
```

Run all modes:

```bash
voicefixer --infile /path/to/input.wav --outfile /path/to/output.wav --mode all
```

For more information:

```bash
voicefixer -h
```

### Python API

```python
from voicefixer import VoiceFixer
voicefixer = VoiceFixer()
# or voicefixer = VoiceFixer(model='voicefixer/voicefixer')
# Mode 0: Original Model (suggested by default)
# Mode 1: Add preprocessing module (remove higher frequency)
# Mode 2: Train mode (might work sometimes on seriously degraded real speech)
for mode in [0,1,2]:
    print("Testing mode",mode)
    voicefixer.restore(
        input=os.path.join(git_root,"test/utterance/original/original.flac"), # low quality .wav/.flac file
        output=os.path.join(git_root,"test/utterance/output/output_mode_"+str(mode)+".flac"), # save file path
        cuda=False, # GPU acceleration
        mode=mode
    )
    if (mode != 2):
        check("output_mode_" + str(mode) + ".flac")
    print("Pass")
```

## License

VoiceFixer 2 is licensed under the **VoiceFixer license**, a license based on the BSD-3-Clause license with an additional restriction on the logo. Although it is not approved by the OSI, it follows the OSI's guidelines for an open source license.

Contributions to this software, including but not limited to pull requests, issues, suggestions, or code contributions, are subject to the following terms:

By submitting contributions to this project, you grant the authors and maintainers of this software the right to use, modify, distribute, sublicense, and otherwise deal with your contributions, including incorporating them into the software at their discretion. You also affirm that your contributions do not infringe on any third-party rights, and you have the necessary permissions to grant these rights.

Your contributions will be subject to the licensing terms determined by the authors and maintainers of this project. You acknowledge that the authors may choose to apply and/or change a license in the future that may differ from the current terms.

This software may include references or links to other open-source repositories or projects. Please note that we do not endorse, verify, or make any warranties regarding the reliability, accuracy, or suitability of these linked projects. You should use them at your own risk and discretion. Any issues, concerns, or liabilities arising from the use of these linked projects are separate from the responsibilities of the authors and maintainers of this software.

This software and its documentation may contain links to external websites or resources that are not maintained or controlled by the authors or maintainers of this project. We do not endorse, verify, or take responsibility for the content, accuracy, or availability of these external links. Clicking on such links is at your own risk, and any use of external websites or resources is subject to their respective terms and conditions.

## Note

Maintenance of VoiceFixer 2 is powered by [NeuralVox](https://github.com/NeuralVox).

## Advertisement

My newest audio-related AI project: TTS API - a open source Tortoise TTS API with streaming support that's coming soon. [Join waitlist](https://github.com/NeuralVox/tts-api). 
