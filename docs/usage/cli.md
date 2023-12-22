# CLI Usage

VoiceFixer 2 has a CLI that allows you to easily restore audio without Python.

```text
Usage: voicefixer [OPTIONS] {file|folder} PATH OUTPUT

Options:
  -m, --mode [0|1|2]
  --help              Show this message and exit.
```

**Modes**

You can find more information about modes in the Modes section under Advanced Usage. The default mode is 0.

**Example 1**

This example will restore `input.wav` and write the output to `output.wav`.

```bash
voicefixer file input.wav output.wav
```

**Example 2**

This example will restore all `.wav` and `.mp3` in the `input` folder and write it to the `output` folder. The folder CLI does not support subdirectories.

```bash
voicefixer folder input output
```

## Legacy CLI

Recently, VoiceFixer 2 introduced a completely new CLI overhaul with breaking changes. You can still access the legacy CLI, however it will be removed in a future release. Please ensure you've locked the version of VoiceFixer 2 in your dependencies to `voicefixer2==2.3.8`.

```text
usage: voicefixer-legacy [-h] [-i INFILE] [-o OUTFILE] [-ifdr INFOLDER]
                         [-ofdr OUTFOLDER] [--mode {0,1,2,all}] [--disable-cuda]
                         [--silent]

VoiceFixer - restores degraded speech

optional arguments:
  -h, --help            show this help message and exit
  -i INFILE, --infile INFILE
                        An input file to be processed by VoiceFixer.
  -o OUTFILE, --outfile OUTFILE
                        An output file to store the result.
  -ifdr INFOLDER, --infolder INFOLDER
                        Input folder. Place all your wav file that need
                        process in this folder.
  -ofdr OUTFOLDER, --outfolder OUTFOLDER
                        Output folder. The processed files will be stored in
                        this folder.
  --mode {0,1,2,all}    mode
  --disable-cuda        Set this flag if you do not want to use your gpu.
  --silent              Set this flag if you do not want to see any message.
```