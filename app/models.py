from typing import List, Optional
from datetime import datetime

# Estrutura do documento no MongoDB
Aula = {
    "nome": str,
    "horario": datetime,
    "limite_vagas": int,
    "inscritos": list[str],
    "presencas": list[str],
}
