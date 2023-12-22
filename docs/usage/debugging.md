# Debugging

::::{note}
If you need support, please do not hesitate to [open an issue](https://github.com/voicefixer/voicefixer/issues) or [discussion](https://github.com/voicefixer/voicefixer/discussions)!
::::

## The resulting audio is unsatisfactory

If the resulting audio is unsatisfactory (ie cut off, mangled, unintelligible), try running the script again, running it in a different mode, or downsampling the original low-quality audio to 22 kHz.

Here's how to downsample audio to 22 kHz with the [ffmpeg](https://ffmpeg.org/) library:

```bash
ffmpeg -i input.wav -ar 22050 output.wav
```