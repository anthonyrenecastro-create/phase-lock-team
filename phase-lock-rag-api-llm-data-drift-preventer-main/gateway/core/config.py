import os
from dataclasses import dataclass


@dataclass(frozen=True)
class GatewaySettings:
    deterministic_mode: bool
    default_seed: int
    drift_spike_threshold: float
    breaker_trip_count: int
    max_metric_window: int
    max_compute_steps: int
    api_key: str | None


def load_settings() -> GatewaySettings:
    api_key = os.getenv("GATEWAY_API_KEY")
    if api_key == "":
        api_key = None

    return GatewaySettings(
        deterministic_mode=os.getenv("DETERMINISTIC_MODE", "true").lower() in {"1", "true", "yes"},
        default_seed=int(os.getenv("DRIFT_ENGINE_SEED", "7")),
        drift_spike_threshold=float(os.getenv("DRIFT_SPIKE_THRESHOLD", "0.80")),
        breaker_trip_count=int(os.getenv("DRIFT_BREAKER_TRIP_COUNT", "3")),
        max_metric_window=int(os.getenv("MAX_METRIC_WINDOW", "4096")),
        max_compute_steps=int(os.getenv("MAX_COMPUTE_STEPS", "50000")),
        api_key=api_key,
    )
