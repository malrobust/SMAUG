from setuptools import setup, find_packages

setup(
    name="sifra",
    version="1.0.0",
    author="Your Name",  # Replace with your name or GitHub handle
    author_email="your.email@example.com",
    description="An autonomous AI security research assistant",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/sifra",
    packages=find_packages(),
    install_requires=[
        "ollama>=0.1.0",
        "chromadb>=0.4.0",
        "pyttsx3>=2.90",
        "openai-whisper>=20231117",
        "beautifulsoup4>=4.12.0",
        "requests>=2.31.0",
        "rich>=13.7.0",
        "prompt_toolkit>=3.0.43",
        "PyYAML>=6.0.1",
    ],
    entry_points={
        "console_scripts": [
            "sifra=main:main_loop",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
    ],
    python_requires=">=3.10",
)
