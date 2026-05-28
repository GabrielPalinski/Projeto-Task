class Task:

    def __init__(
        self,
        title,
        description,
        priority,
        status="Pendente"
    ):

        self.title = title

        self.description = description

        self.priority = priority

        self.status = status