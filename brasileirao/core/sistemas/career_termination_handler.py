class CareerTerminationHandler:
    RETIREMENT_TYPES = {
        "glorious": {"min_trophies": 5, "min_overall": 80},
        "dramatic": {"max_morale": 30, "injury_prone": True},
        "scandalous": {"active_scandals": True},
    }

    def handle_retirement(self, player):
        retirement_type = self._determine_retirement_type(player)
        event_script = self._generate_retirement_script(player, retirement_type)

        if retirement_type == "glorious":
            player.club.fan_happiness += 15
            player.nation.football_legacy += 10
        elif retirement_type == "scandalous":
            player.club.reputation -= 25
            SponsorshipImpactSimulator.apply_penalties(player.club)

        BroadcastSystem.live_event(event=event_script, production_quality="cinematic")

    def _determine_retirement_type(self, player):
        return "glorious"

    def _generate_retirement_script(self, player, retirement_type):
        return f"{player.nome} retired as {retirement_type}"


class SponsorshipImpactSimulator:
    @staticmethod
    def apply_penalties(club):
        pass


class BroadcastSystem:
    @staticmethod
    def live_event(event, production_quality="standard"):
        pass
