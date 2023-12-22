| NOTE: Breaking changes to the CLI + API! Please read the documentation for more details! The old CLI is still available through the `voicefixer-legacy` command.
| ---

**Important:** The maintainers(s) of this repository are not affiliated or connected with the original version of VoiceFixer.

# <img src="https://camo.githubusercontent.com/a3b2d4da7e2d171fd691b5d2da5af46013dcb7904132485a3af7d14b6468aeac/68747470733a2f2f6769746875622d70726f64756374696f6e2d757365722d61737365742d3632313064662e73332e616d617a6f6e6177732e636f6d2f37363138363035342f3237303230343034382d34393962333538642d303036332d343562632d393235622d6434313336633035616633342e706e67" width="30"> VoiceFixer 2

**[Docs](https://voicefixer.github.io/voicefixer/)**

Welcome to VoiceFixer 2, the next generation of VoiceFixer. VoiceFixer is a general speech restoration tool, using AI to remove background noise, fix degraded speech, enhance audio quality from old recordings, upscale audio resolution, and more, all in one model!

VoiceFixer aims to restore human speech, regardless of how seriously degraded it is. It can handle noise, reverberation, low resolution, and clipping effect within one model!

## What's different from the original VoiceFixer?

The [original version of VoiceFixer](https://github.com/haoheliu/voicefixer) continues to be updated with minor changes and bug fixes. VoiceFixer 2 adds major new features (including Apple Silicon support, a revamped CLI, and more) and fixes several bugs.

### New features in VoiceFixer 2

We’ve added the following features in VoiceFixer 2:

* We’ve added MPS support, which means you can use GPU acceleration on macOS devices running on Apple Silicon chips.
* Revamped CLI.
* Documentation
* We've added a progress bar through TQDM for longer audio
* We now support non-WAV files (ie MP3)
* We're now using `cached_path` instead of using a hard-coded a cache path to increase OS support
* We're featuring much faster model downloads w/ Hugging Face (the original VoiceFixer models are hosted on Zenodo)
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

- [ ] Fine-tune model for better results (this one requires compute - see [this](https://github.com/haoheliu/voicefixer_main) training repo)
- [x] Add MP3 support for folders
- [x] Allow user to restore an object (don't require a file)
- [ ] Allow user to input audio as an audio object, wave object, numpy array, torchaudio object, or pydub object and to output audio in varied formats as well, similar to how Gradio can accept audio in many different formats
- [ ] Update model to make [modifying state dict](https://github.com/voicefixer/voicefixer/commit/1b8c384bc2f34645e72c67e46db92b3accd20613) unnecessary - loading it twice increases VRAM usage (related to latest librosa issue)
    - [ ] Update model
    - [ ] Remove code
- [ ] [Realtime support](https://github.com/haoheliu/voicefixer_main/issues/11)
- [ ] [Add to HF Audio-to-Audio pipeline](https://huggingface.co/docs/hub/models-adding-libraries)
- [x] Support Windows (mostly file paths) - maybe use [cached_path](https://github.com/allenai/cached_path)
    - [ ] Fully test on Windows
- [x] Clean up CLI (may have breaking changes)
- [x] Support custom models
- [x] Use latest version of librosa (probably pretty important, here's the issue the model doesn't work with latest torchlibrosa and the old torchlibrosa doesn't work with the latest librosa. need to completely retrain the model probably or change model python file) - fixed thanks to @manmay-nakhashi
- [x] Switch models from Zenodo to Hugging Face to increase speed and control over models (in progress)
- [x] Publish to pip
- [x] Add TQDM progress bar - crucial for longer conversions
- [x] Implement .mp3 support (currently only supports .wav)
- [x] Fix CLI instead of copying to /bin use CLI like [this](https://github.com/fakerybakery/simplesplit/blob/main/setup.py)

## Usage

If you'd just like to process a single file, try our live demo or REST API. Please see the Hosted Services section below for details.

### Documentation

Please visit our [documentation](https://voicefixer.github.io/voicefixer/) for examples, a quick start guide, and more!

### Installation

Please refer to the [documentation](https://voicefixer.github.io/voicefixer/get-started/install.html).

**NOTE: When installing from PyPI, make sure to install `voicefixer2`.**

## Usage

**Important:** FFmpeg must be installed to support non-.wav files.

### Command Line

Please see the [documentation](https://voicefixer.github.io/voicefixer/usage/cli.html).

### Python API

Please see the [documentation](https://voicefixer.github.io/voicefixer/usage/api/basic.html).

## Hosted Services

VoiceFixer 2 provides free hosted services. The reliability of these services is not guaranteed.

### Live Demo

[Check out the demos to see what VoiceFixer can do!](https://voicefixer.github.io/)

### REST API

**Don't want to install the package, but just want to try it out?**

Use our free API (no API key required) for audio files under 5 minutes. Non-commercial use only, audio may be collected. Details on [webpage](https://huggingface.co/spaces/voicefixer/voicefixer-api).

```bash
curl -X POST -H "Content-Type: multipart/form-data" -F "file=@test.mp3" https://voicefixer-voicefixer-api.hf.space/process_audio > processed_audio.wav
```

The hosted service is subject to the [REST API Terms of Use](https://voicefixer.github.io/voicefixer/api/terms.html).

## License

VoiceFixer 2 is licensed under the **VoiceFixer license**, a permissive license based on the BSD-3-Clause license with an additional restriction on the logo.

## Contribution Policy

By submitting contributions, you agree to the [docs/contributing.md](Contribution Policy).

## Note

Maintenance of VoiceFixer 2 is powered by [NeuralVox](https://github.com/NeuralVox).

## Advertisement

My newest audio-related AI project: TTS API - a open source Tortoise TTS API with streaming support that's coming soon. [Join waitlist](https://github.com/NeuralVox/tts-api). 
