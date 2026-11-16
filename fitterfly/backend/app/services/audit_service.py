from datetime import UTC, datetime


class AuditService:
    def record(self, action: str, entity_type: str, entity_id: str | int | None, metadata: dict) -> dict:
        return {
            "action": action,
            "entity_type": entity_type,
            "entity_id": str(entity_id) if entity_id is not None else None,
            "metadata": metadata,
            "recorded_at": datetime.now(UTC).isoformat(),
        }
