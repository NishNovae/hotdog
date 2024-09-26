[project]
name = "hnh"
version = "0.3.0"
description = "Default template for PDM package"
authors = [
    {name = "NishNovae", email = "raecrowned@gmail.com"},
]
dependencies = [
    "fastapi>=0.115.0",
    "uvicorn>=0.30.6",
    "transformers==4.44.2",
    "torch>=2.4.1",
    "torchvision>=0.19.1",
    "nvidia-curand-cu12>=10.3.2.106",
]
requires-python = ">=3.11"
readme = "README.md"
license = {text = "MIT"}


[tool.pdm]
distribution = true
