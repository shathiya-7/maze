class ScoringSystem:
    def calculate_score(self, path_length, path_cost, nodes_explored, difficulty_multiplier=1.0):
        # Base score for finishing
        score = 1000
        # Penalties for efficiency
        score -= (path_length * 10)
        score -= (path_cost * 5)
        score -= (nodes_explored * 0.5)
        return max(0, int(score * difficulty_multiplier))
