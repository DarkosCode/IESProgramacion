import random

class RockPaperScissorsGame:
    def __init__(self):
        self.user_score = 0
        self.cpu_score = 0
        self.choices = ["Piedra", "Papel", "Tijera"]

    def get_cpu_choice(self):
        """Genera una elección aleatoria para la CPU."""
        return random.choice(self.choices)

    def determine_winner(self, user_choice, cpu_choice):
        """
        Determina el ganador de la ronda.
        :param user_choice: Elección del usuario (str)
        :param cpu_choice: Elección de la CPU (str)
        :return: 'Usuario', 'CPU', o 'Empate'
        """
        if user_choice not in self.choices:
            return "Error: Elección inválida"

        if user_choice == cpu_choice:
            return "Empate"
        
        # Reglas: Piedra > Tijera, Papel > Piedra, Tijera > Papel
        if (user_choice == "Piedra" and cpu_choice == "Tijera") or \
           (user_choice == "Papel" and cpu_choice == "Piedra") or \
           (user_choice == "Tijera" and cpu_choice == "Papel"):
            self.user_score += 1
            return "Usuario"
        else:
            self.cpu_score += 1
            return "CPU"
            
    def get_scores(self):
        return self.user_score, self.cpu_score
        
    def reset_scores(self):
        self.user_score = 0
        self.cpu_score = 0
