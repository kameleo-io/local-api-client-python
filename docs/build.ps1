autorest --verbose --input-file=./docs/swagger.json --python --output-folder=./output --namespace=kameleo.local_api_client --override-client-name=KameleoLocalApiClient  --package-name=kameleo.local_api_client --legacy
Copy-Item -Force -Recurse -Path .\\output\* -Destination .
Remove-Item -Force -Recurse -Path .\\output
