from pydantic import BaseModel, Field
from app.schemas.decision import Decision


class ScreeningRequest(BaseModel):
    component_id: str
    lot_id: str

    value_0h: float = Field(...)
    value_24h: float = Field(...)
    value_96h: float = Field(...)


class ScreeningResponse(BaseModel):
    component_id: str
    lot_id: str

    module_a_decision: Decision
    module_a_anomaly_score: float

    module_b_decision: Decision
    predicted_168h: float
    predicted_drift: float

    final_decision: Decision
    risk_level: str

    explanation: list[str]


class BatchScreeningRequest(BaseModel):
    components: list[ScreeningRequest]


class BatchSummary(BaseModel):
    total_components: int
    pass_count: int
    flag_count: int
    pending_count: int
    error_count: int


class BatchScreeningResponse(BaseModel):
    summary: BatchSummary
    results: list[ScreeningResponse]

