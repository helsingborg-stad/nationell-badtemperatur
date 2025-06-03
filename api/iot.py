import json
import os
from datetime import datetime

from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.security import APIKeyHeader

from api.models.geo import GeoModel
from api.models.get_response import BadTempGetResponseModel
from api.models.ld import LdModel
from api.models.post_response import BadTempPostResponseModel

iot_router = APIRouter(prefix="/iot", tags=["iot"])

JSON_SCHEMA_REF_TEMPLATE = "#/components/schemas/{model}"

OPENAPI_EXTRA = {
    "requestBody": {
        "content": {
            "application/geo+json": {
                "schema": GeoModel.model_json_schema(ref_template=JSON_SCHEMA_REF_TEMPLATE)},
            "application/ld+json": {
                "schema": LdModel.model_json_schema(ref_template=JSON_SCHEMA_REF_TEMPLATE)},
            "application/json": None,
        }
    }
}

header_scheme = APIKeyHeader(name="X-API-Key")

secret_api_key = "secret"


@iot_router.post("/badtemp", response_model=BadTempPostResponseModel, openapi_extra=OPENAPI_EXTRA)
async def badtemp(body: LdModel | GeoModel, request: Request, api_key: str = Depends(header_scheme)):
    if api_key != secret_api_key:
        raise HTTPException(status_code=400, detail="X-API-Key header invalid")

    print(api_key)

    content_type = request.headers.get("Content-Type")
    file_ext = "json"
    dir_name = "unknown"

    if content_type == "application/ld+json":
        file_ext = "ldjson"
        ld_data = LdModel.model_validate(json.loads(await request.body()))
        dir_name = ld_data.graph[0].dcterms_identifier
    elif content_type == "application/geo+json":
        file_ext = "geojson"
        dir_name = body.features[0].properties.name

    result_directory = f"data/{dir_name}"
    os.makedirs(result_directory, exist_ok=True)
    current_date = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(os.path.join(result_directory, f"{current_date}.{file_ext}"), "w") as file:
        file.write(body.model_dump_json(by_alias=True))

    return BadTempPostResponseModel(received=True)


@iot_router.get("/badtemp", response_model=BadTempGetResponseModel)
async def badtemp():
    return BadTempGetResponseModel(data="Hello, World!")
