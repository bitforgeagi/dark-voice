from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="dark-voice-demo",
    version="0.1.0",
    author="Bitforge Dynamics LLC",
    author_email="brock@bitforgedynamics.com",
    description="A demo application for Dark Voice TTS GUI using the Kokoro-82M model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bitforgeagi/dark-voice",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.11",
    install_requires=requirements,
) 