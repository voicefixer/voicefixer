# Methods

## `VoiceFixer()`

1. **`__init__`**
   - Initializes the VoiceFixer model.
   - Parameters:
     - `model` (str): Path or identifier for the pre-trained model. Default: `voicefixer/voicefixer`

2. **`restore_inmem`**
   - Restores the input waveform using the VoiceFixer model.
   - Parameters:
     - `wav_10k` (numpy.ndarray): Input waveform with a sample rate of 10,000 Hz.
     - `cuda` (bool): Flag indicating whether to use CUDA (default is True).
     - `mode` (int): Mode of operation (0, 1, or 2).
     - `your_vocoder_func` (function): Optional external vocoder function.
     - `tqdm` (function): Progress bar function (default is tqdm).
   - Returns:
     - numpy.ndarray: Restored waveform.

3. **`restore`**
   - Restores the waveform from the input file and saves it to the output file.
   - Parameters:
     - `input` (str): Path to the input waveform file.
     - `output` (str): Path to save the output waveform file.
     - `cuda` (bool): Flag indicating whether to use GPU (default is False). Supports CUDA, MPS (Apple Silicon), and ROCM.
     - `mode` (int): Mode of operation (0, 1, or 2). See the Advanced Usage guide for more details.
     - `tqdm` (function): Progress bar function (default is tqdm). This is useful if you need to display progress using a custom method.