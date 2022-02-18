# Rest client generation

Generate Python client for Kameleo Rest API.

## Build instructions

### Step 1

```powershell
npm install -g autorest
```

### Step 2

Update the swagger.json

### Step 3

```powershell
.\build.ps1
```

## Notes

* Generate code based on `V2` version, you can add `--legacy` flag to the command line to get the previous behavior.
* You may have to use the beta version of autorest with specific node versions: `autorest --version=beta`

## Publish instructions

### Step 0: Install in development mode

```powershell
python -m pip install -e .
```

### Step 1: Packaging for publish

```powershell
python setup.py sdist
```

## Step 2: Packaging for publish

```powershell
python setup.py bdist_wheel --universal
```

## Step 3: Upload package to package manager

```powershell
twine upload dist/*
```

You may explicitly tell which version to upload
