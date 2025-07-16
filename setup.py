import os
import subprocess
import sys
from pathlib import Path
from typing import Union

from setuptools import find_packages, setup


def get_sha(root_dir: Union[str, Path]) -> str:
    try:
        return (
            subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root_dir)
            .decode("ascii")
            .strip()
        )
    except Exception:
        return 'UNKNOWN'


def parse_requirements(filename):
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


def main():
    package_name = 'yolov9-vx'
    install_reqs = parse_requirements("./requirements.txt")
    print(os.path.join(os.path.dirname(__file__), package_name))

    sys.path.insert(0, os.path.join(os.path.dirname(__file__), package_name))
    import yolov9_vx

    package_version = yolov9_vx.__version__
    if package_version == 'REPLACE':
        default_version = '0.0.1'
        sha = get_sha(Path.cwd())
        if sha == 'UNKNOWN':
            package_version = f'{default_version}+dev'
        else:
            package_version = f'{default_version}+git{sha[:7]}'
    
    setup(
        name=package_name,
        version=package_version,
        description="YOLOv9 models, utilities and tools package",
        url='https://github.com/vexcel-data/yolov9.git',
        author='ML team',
        python_requires=">=3.8",
        install_requires=[install_reqs],
        include_package_data=True,
        packages=[
            'yolov9_vx',
            'yolov9_vx.models',
            'yolov9_vx.utils',
            'yolov9_vx.utils.segment',
            'yolov9_vx.utils.panoptic',
            'yolov9_vx.utils.tal',
            'yolov9_vx.utils.loggers',
            'yolov9_vx.utils.loggers.clearml',
            'yolov9_vx.utils.loggers.comet',
            'yolov9_vx.utils.loggers.wandb',
            'yolov9_vx.tools'
        ],
        package_dir={
            'yolov9_vx': 'yolov9_vx',
            'yolov9_vx.models': 'models',
            'yolov9_vx.utils': 'utils',
            'yolov9_vx.utils.segment': 'utils/segment',
            'yolov9_vx.utils.panoptic': 'utils/panoptic',
            'yolov9_vx.utils.tal': 'utils/tal',
            'yolov9_vx.utils.loggers': 'utils/loggers',
            'yolov9_vx.utils.loggers.clearml': 'utils/loggers/clearml',
            'yolov9_vx.utils.loggers.comet': 'utils/loggers/comet',
            'yolov9_vx.utils.loggers.wandb': 'utils/loggers/wandb',
            'yolov9_vx.tools': 'tools'
        },
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
        package_data={
            'yolov9_vx': ['*.yaml', '*.yml'],
            'yolov9_vx.models': ['**/*.yaml', '**/*.yml'],
            'yolov9_vx.utils': ['**/*.yaml', '**/*.yml'],
            'yolov9_vx.tools': ['**/*.yaml', '**/*.yml', '**/*.ipynb'],
        },
)


if __name__ == '__main__':
    # Make sure that wheel package is installed python3 -m pip install wheel
    # python3 setup.py bdist_wheel
    main()
