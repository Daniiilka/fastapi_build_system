# Build-system

A FastAPI system that automates and accelerates the routine processes of building applications

## Installation

To setup environment and install package dependencies run setup.sh

```bash
bash setup.sh
```

## Usage

You can run FastAPI app manually by this command:
```bash
cd {PATH TO THE PROJECT}
# startapp
bash start.sh
```
You can send post request to the API with the template below with the actual build name instead of example data "any_build_name":
```json
{
    "build": "any_build_name"
}
```

## Tests
You can run tests by command below:
```bash
cd {PATH TO THE PROJECT}
pytest
```