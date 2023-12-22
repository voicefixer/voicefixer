import click
import os
from glob import glob


@click.command()
@click.argument("type", type=click.Choice(["file", "folder"], case_sensitive=False))
@click.argument("path", type=click.Path(exists=True))
@click.argument("output", type=click.Path(exists=False))
@click.option("--mode", "-m", type=click.Choice([0, 1, 2]), default=0)
def main(type, path, output, mode):
    from voicefixer import VoiceFixer
    import torch

    gpu_available = torch.cuda.is_available() or torch.backends.mps.is_available()
    voicefixer = VoiceFixer()
    if type == "file":
        voicefixer.restore(
            input=path, output=output, cuda=gpu_available, mode=int(mode)
        )
    else:
        # scan directory
        files = glob(os.path.join(path, "*.wav", recursive=True)) + glob(
            os.path.join(path, "*.mp3", recursive=True)
        )
        for file in files:
            voicefixer.restore(
                input=file,
                output=os.path.basename(file),
                cuda=gpu_available,
                mode=int(mode),
            )


if __name__ == "__main__":
    main()
