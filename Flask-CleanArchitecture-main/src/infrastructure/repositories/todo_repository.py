from domain.models.itodo_repository import ITodoRepository
from domain.models.todo import Todo
from typing import List, Optional

class TodoRepository(ITodoRepository):
    def __init__(self):
        self._todos = []
        self._id_counter = 1

    def add(self, todo: Todo) -> Todo:
        todo.id = self._id_counter
        self._id_counter += 1
        self._todos.append(todo)
        return todo

    def get_by_id(self, todo_id: int) -> Optional[Todo]:
        for todo in self._todos:
            if todo.id == todo_id:
                return todo
        return None

    def list(self) -> List[Todo]:
        return self._todos

    def update(self, todo: Todo) -> Todo:
        for idx, t in enumerate(self._todos):
            if t.id == todo.id:
                self._todos[idx] = todo
                return todo
        raise ValueError('Todo not found')

    def delete(self, todo_id: int) -> None:
        self._todos = [t for t in self._todos if t.id != todo_id]