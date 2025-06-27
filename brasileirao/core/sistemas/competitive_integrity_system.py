import random
from ..entidades.time import Time
from .financial_regulation_framework import aplicar_multa_esquema


def verificar_esquema_apostas(time: Time) -> bool:
    if time.sorte == 20:
        return False
    chance = max(0.01, (20 - time.factor_torcida) * 0.02)
    if random.random() < chance:
        gravidade = random.choice([1, 2, 3, 4, 5])
        aplicar_punicao(time, gravidade)
        return True
    return False


def aplicar_punicao(time: Time, gravidade: int):
    time.factor_orcamento = max(0, time.factor_orcamento - gravidade)
    time.factor_torcida = max(0, time.factor_torcida - gravidade)
    aplicar_multa_esquema(time, gravidade)


class SportsIntegrityAgency:
    """Agência simplificada para investigações de integridade esportiva."""

    STEP_1 = "Coleta de provas digitais"
    STEP_5 = "Análise de padrões de aposta"
    STEP_10 = "Aplicação de sanções em cadeia"

    def __init__(self) -> None:
        self.active_investigations = []
        self.sanctions_database = SanctionRegistry()

    def launch_investigation(self, target, allegation_type: str):
        """Inicia investigação considerando conexões pré-existentes."""
        for existing_inv in self.active_investigations:
            if self._check_connections(target, existing_inv):
                existing_inv.expand_scope(target)
                return

        new_inv = IntegrityInvestigation(
            targets=[target], allegation=allegation_type, risk_level=random.randint(30, 90)
        )
        self.active_investigations.append(new_inv)
        self._notify_governing_body(new_inv)

    def apply_sanctions(self, investigation_id: str):
        investigation = self._get_investigation(investigation_id)
        if investigation is None:
            return
        final_report = investigation.generate_final_report()
        for entity in final_report.guilty_parties:
            sanction = self.sanctions_database.get_sanction(
                entity_type=type(entity), offense_level=final_report.severity_score
            )
            entity.apply_sanction(sanction)
            ReputationImpactSimulator.apply_ripple_effect(entity, sanction)

    # Métodos simplificados de apoio -------------------------
    def _notify_governing_body(self, investigation):
        pass  # placeholder

    def _get_investigation(self, investigation_id: str):
        for inv in self.active_investigations:
            if getattr(inv, "id", None) == investigation_id:
                return inv
        return None

    def _check_connections(self, target, existing_inv) -> bool:
        return False


class SanctionRegistry:
    def get_sanction(self, entity_type, offense_level):
        return {
            "ban_length": offense_level * 2,
            "fine": offense_level * 1_000_000,
        }


class IntegrityInvestigation:
    def __init__(self, targets, allegation, risk_level):
        self.id = f"INV-{random.randint(1000, 9999)}"
        self.targets = targets
        self.allegation = allegation
        self.risk_level = risk_level

    def expand_scope(self, target):
        if target not in self.targets:
            self.targets.append(target)

    def generate_final_report(self):
        class Report:
            guilty_parties = self.targets
            severity_score = self.risk_level // 10

        return Report()


class ReputationImpactSimulator:
    @staticmethod
    def apply_ripple_effect(entity, sanction):
        pass  # placeholder for complex logic
