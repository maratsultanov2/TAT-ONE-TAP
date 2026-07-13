from setuptools import setup, find_packages

setup(
    name="tat-one-tap",
    version="1.0.0",
    author="Marat Sultanov",
    description="Ecosystem of modules for memory management and structural analysis in AI agents",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/maratsultanov2/TAT-ONE-TAP",
    packages=find_packages(include=["tat", "tat.*", "tat_monitor", "tat_defense", "tat_diff"]),
    install_requires=[
        "numpy>=1.21.0",
        "torch>=1.10.0",
        "sentence-transformers>=2.2.0",
        "scikit-learn>=1.0.0",
        "pandas>=1.3.0",
        "matplotlib>=3.5.0",
        "seaborn>=0.11.0",
        "fastapi>=0.85.0",
        "uvicorn>=0.18.0",
        "requests>=2.28.0",
    ],
    python_requires=">=3.8",
    license="Proprietary / AGPL-3.0 (see LICENSE)",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
