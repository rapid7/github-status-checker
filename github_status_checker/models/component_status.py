from enum import Enum


class ComponentStatus(Enum):
    operational = "operational"
    degraded = "degraded_performance"
    partial_outage = "partial_outage"
    major_outage = "major_outage"
