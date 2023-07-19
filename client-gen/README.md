client is generated using the following command

```shell
docker run --rm  -ti  -v ${PWD}:/local openapitools/openapi-generator-cli  generate  -i /local/openapi.json -g
 python -o /local/client/
```