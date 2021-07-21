# Build instructions
## Step 1
```
npm install -g autorest
```

## Step 2
Update the swagger.json

## Step 3
```
.\build.ps1
```

# Notes
You may have to use the beta version of autorest with specific node versions: `autorest --version=beta`

# Publish instructions
## Step 1
```
python setup.py sdist
```

## Step 2
```
python setup.py bdist_wheel --universal
```

## Step 3
```
twine upload dist/*
```
You may explicitly tell which version to upload