# Missão de sala • Squad UrbanInventory
# Base de teste com 4 equipamentos (ID, tipo, dias de revisão, status de revisão)
equipamentos = [
    {"id": "Respirador 1", "setor": "UTI", "dias": 45, "revisado": True},
    {"id": "Respirador 2", "setor": "UTI", "dias": 210, "revisado": True},
    {"id": "Bomba 1", "setor": "Triagem", "dias": 30, "revisado": False},
    {"id": "Monitor 1", "setor": "UTI", "dias": 100, "revisado": True}
]

# Tarefa 1: 
todos_no_prazo = all(eq["dias"] < 180 for eq in equipamentos)
print(f"1. Todos os equipamentos estão no prazo de revisão? {todos_no_prazo}")

# Tarefa 2:
uti_sem_revisao = any(eq["setor"] == "UTI" and not eq["revisado"] for eq in equipamentos)
print(f"2. Existe algum equipamento da UTI sem revisão? {uti_sem_revisao}")

# Tarefa 3:
ids_com_problema = [eq["id"] for eq in equipamentos if not eq["revisado"] or eq["dias"] > 180]
print(f"3. IDs dos equipamentos com problema: {ids_com_problema}")
