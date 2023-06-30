# Build-system

A FastAPI system that automates and accelerates the routine processes of building applications

## Installation

To setup environment and install package dependencies run setup.sh

```bash
./setup.sh
```

## Usage

You can run FastAPI app manually by this command:
```bash
cd {PATH TO THE PROJECT}
# startapp
uvicorn main:app --reload --port 5000
```
Or you can start tmux session by the command below:
```bash
./tmux-build-system.sh
```
For tmux startapp you should edit ./tmux-build-system.sh with the path for the project directory first

## Tests
You can run tests by command below:
```bash
cd {PATH TO THE PROJECT}
pytest
```