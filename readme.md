# Build-system

A FastAPI system that automates and accelerates the routine processes of building applications

## Installation

To setup environment and install package dependencies run setup.sh

```bash
bash setup.sh
```

## Usage

You can run FastAPI app manually by this command, It will start the application on the 5000 port:
```bash
bash start.sh
```

You can send post request to /get_tasks route of the API with the template below with the actual build name instead of example data "any_build_name":
```json
{
    "build": "any_build_name"
}
```

## Tests
You can run tests by command below:
```bash
source venv/bin/activate

pytest
```