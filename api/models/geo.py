from pydantic import BaseModel


class GeoModel(BaseModel):
    class Features(BaseModel):
        type: str | None = None

        class Geometry(BaseModel):
            type: str | None = None
            coordinates: list[float] | None = None

        geometry: Geometry | None = None

        class Properties(BaseModel):
            name: str | None = None
            temperature: float | None = None
            reportedAt: str | None = None
            batteryLevel: int | None = None
            deviceType: str | None = None

        properties: Properties | None = None

    type: str | None = None
    features: list[Features] | None = None
