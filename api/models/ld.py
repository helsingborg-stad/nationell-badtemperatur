from pydantic import BaseModel, Field


class LdModel(BaseModel):
    class Graph(BaseModel):
        class BrickLastKnownValue(BaseModel):
            class QudtHasUnit(BaseModel):
                class RdfsLabel(BaseModel):
                    value: str | None = Field(alias="@value", default=None)
                    language: str | None = Field(alias="@language", default=None)

                id: str | None = Field(alias="@id", default=None)
                type: str | None = Field(alias="@type", default=None)
                rdfs_label: list[RdfsLabel] | None = Field(alias="rdfs:label", default=None)
                qudt_symbol: str | None = Field(alias="qudt:symbol", default=None)

            type: str | None = Field(alias="@type", default=None)
            brick_timestamp: str | None = Field(alias="@brick:timestamp", default=None)
            qudt_value: float | None = Field(alias="qudt:value", default=None)
            qudt_hasUnit: QudtHasUnit | None = Field(alias="qudt:hasUnit", default=None)

        class SchemaGeo(BaseModel):
            type: str | None = Field(alias="@type", default=None)
            schema_latitude: float | None = Field(alias="schema:latitude", default=None)
            schema_longitude: float | None = Field(alias="schema:longitude", default=None)

        id: str | None = Field(alias="@id", default=None)
        type: str | None = Field(alias="@type", default=None)
        dcterms_identifier: str | None = Field(alias="dcterms:identifier", default=None)
        schema_additionalType: str | None = Field(alias="schema:additionalType", default=None)
        brick_lastKnownValue: BrickLastKnownValue | None = Field(alias="brick:lastKnownValue", default=None)
        schema_geo: SchemaGeo | None = Field(alias="schema:geo", default=None)
        dcterms_relation: str | None = Field(alias="dcterms:relation", default=None)

    class Context(BaseModel):
        rdfs: str | None = None
        qudt: str | None = None
        prov: str | None = None
        rdf: str | None = None
        dcterms: str | None = None
        bt_schema: str | None = Field(alias="schema", default=None)
        geodcatap: str | None = None
        brick: str | None = None
        rec: str | None = None

    context: Context | None = Field(alias="@context", default=None)
    graph: list[Graph] | None = Field(alias="@graph", default=None)
