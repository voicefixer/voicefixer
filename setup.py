import io
import os
from setuptools import find_packages, setup

NAME = "voicefixer2"
DESCRIPTION = "General speech restoration toolkit."
URL = "https://github.com/voicefixer/voicefixer"
EMAIL = "me@mrfake.name"
AUTHOR = "mrfakename"
REQUIRES_PYTHON = ">=3.7.0"
VERSION = "2.3.8"
REQUIRED = [
    "matplotlib",
    "cached_path",
    "torch>=1.7.0",
    "progressbar",
    "torchlibrosa",
    "GitPython",
    "streamlit",
    "pyyaml",
    "pydub",
    "scipy",
    "soundfile",
    "librosa",
]
EXTRAS = {
    'docs': [
        'sphinxawesome-theme',
        'myst-parser'
    ]
}
here = os.path.abspath(os.path.dirname(__file__))
try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION

setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    py_modules=["voicefixer"],
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    packages=find_packages(),
    include_package_data=True,
    license="VoiceFixer (BSD-3 + logo restriction)",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    entry_points={
        "console_scripts": [
            "voicefixer = voicefixer.cli:main",
        ],
    },
)
