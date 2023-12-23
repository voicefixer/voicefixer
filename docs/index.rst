VoiceFixer 2
============

.. note::

   VoiceFixer 2 documentation is in beta. We plan to add more documentation in the future.

.. rst-class:: lead

   A toolkit for general speech restoration.

Welcome to VoiceFixer 2, a toolkit for general speech restoration. VoiceFixer 2 is based on Haohe Liu's original `VoiceFixer <https://github.com/haoheliu/voicefixer>`_ project

Installation
------------

Quickly try out VoiceFixer 2 by running:

.. code-block:: bash

   pip install voicefixer2

For more details, please see the Installation section.

Features
--------

**GPU-Accelerated:** VoiceFixer 2 supports a wide range of GPUs, from Apple Silicon computers to Nvidia and AMD GPUs. This allows the VoiceFixer 2 to run more quickly and efficiently!

**Offline:** VoiceFixer 2 runs offline. Internet is only required to download the restoration model. This means you can enhance audio files on-the-go, without needing to connect to the internet!

**Single Model:** Traditionally, GSR (General Speech Restoration) tools have utilized multiple AI models. VoiceFixer and VoiceFixer 2 only use one single model to handle all restoration tasks. This makes it more efficient, faster, and easier to use!

Samples
-------

Here are some examples of what VoiceFixer 2 can do:

+-----------------------------------------+-----------------------------------------------+
| Before                                  | After                                         |
+=========================================+===============================================+
| .. raw:: html                           | .. raw:: html                                 |
|                                         |                                               |
|   <audio controls="controls">           |   <audio controls="controls">                 |
|         <source src="_static/001.mp3">  |         <source src="_static/001_fixed.mp3">  |
|         Your browser does not support   |         Your browser does not support the     |
|         the <code>audio</code> element. |         <code>audio</code> element.           |
|   </audio>                              |   </audio>                                    |
+-----------------------------------------+-----------------------------------------------+
| .. raw:: html                           | .. raw:: html                                 |
|                                         |                                               |
|   <audio controls="controls">           |   <audio controls="controls">                 |
|         <source src="_static/002.mp3">  |         <source src="_static/002_fixed.mp3">  |
|         Your browser does not support   |         Your browser does not support the     |
|         the <code>audio</code> element. |         <code>audio</code> element.           |
|   </audio>                              |   </audio>                                    |
+-----------------------------------------+-----------------------------------------------+
| .. raw:: html                           | .. raw:: html                                 |
|                                         |                                               |
|   <audio controls="controls">           |   <audio controls="controls">                 |
|         <source src="_static/003.mp3">  |         <source src="_static/003_fixed.mp3">  |
|         Your browser does not support   |         Your browser does not support the     |
|         the <code>audio</code> element. |         <code>audio</code> element.           |
|   </audio>                              |   </audio>                                    |
+-----------------------------------------+-----------------------------------------------+


Table of Contents
-----------------
.. dropdown:: Table of Contents

   .. toctree::
      :maxdepth: 1
      :caption: Get Started
      
      get-started/install.md
      get-started/quickstart.md

   .. toctree::
      :maxdepth: 2
      :caption: Usage

      usage/cli.md
      usage/api/index.rst
      usage/advanced/index.rst
      usage/debugging.md
   
   .. toctree::
      :maxdepth: 1
      :caption: Updates

      news.md
      changelog.md

   .. toctree::
      :maxdepth: 2
      :caption: REST API

      api/index.md
      api/terms.md
      api/usage.md

   .. toctree::
      :maxdepth: 1
      :caption: Project
      
      Source Code (GitHub) <https://github.com/voicefixer/voicefixer>
      Live Demo <https://huggingface.co/spaces/voicefixer/voicefixer>
      Free API <https://huggingface.co/spaces/voicefixer/voicefixer-api>
      license.md
      contributing.md
      faq.md
      press.md
      X <https://twitter.com/voicefixer2>

   .. toctree::
      :maxdepth: 1
      :caption: Support
      
      GitHub Issues <https://github.com/voicefixer/voicefixer/issues>
      GitHub Discussions <https://github.com/voicefixer/voicefixer/discussions>
