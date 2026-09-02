from app.schemas.decision import Decision


class FusionService:

    def evaluate(
        self,
        module_a_result,
        module_b_result
    ):

        # Never treat unavailable modules as PASS.

        if (
            module_a_result.decision == Decision.ERROR
            or module_b_result.decision == Decision.ERROR
        ):
            return {
                "final_decision": Decision.ERROR,
                "risk_level": "UNKNOWN",
                "explanation": [
                    "One or more screening modules encountered an error."
                ]
            }

        if (
            module_a_result.decision == Decision.PENDING
            or module_b_result.decision == Decision.PENDING
        ):
            return {
                "final_decision": Decision.PENDING,
                "risk_level": "UNKNOWN",
                "explanation": [
                    "One or more screening modules are not yet available."
                ]
            }

        # Actual screening decision.
        if (
            module_a_result.decision == Decision.FLAG
            or module_b_result.decision == Decision.FLAG
        ):
            return {
                "final_decision": Decision.FLAG,
                "risk_level": "HIGH",
                "explanation": [
                    "One or more screening modules detected elevated risk."
                ]
            }

        return {
            "final_decision": Decision.PASS,
            "risk_level": "LOW",
            "explanation": [
                "Both screening modules indicate acceptable behavior."
            ]
        }

