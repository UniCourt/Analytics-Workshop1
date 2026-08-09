import React, { Fragment, useEffect, useState } from "react";
import EditTodo from "./EditTodo";

export default function ListTodos() {
  const [todos, setTodos] = useState([]);

  //delete function

  const deleteTodo = async (id) => {
    try {
      const deleteTodo = await fetch(`http://localhost:5000/todos/${id}`, {
        method: "DELETE",
      });
      setTodos(todos.filter(todo => todo.todoid !== id));
    } catch (err) {
      console.error(err.message);
    }
  };

  const getTodos = async () => {
    try {
      const response = await fetch("http://localhost:5000/todos");
      const jsonData = await response.json();

      setTodos(jsonData);
    } catch (err) {
      console.error(err.message);
    }
  };

  useEffect(() => {
    getTodos();
  }, []);
  //   console.log(todos);
  return (
    <Fragment>
      <table className="table table-striped mt-5 text-center">
        <thead>
          <tr>
            <th>Description </th>
            <th>Edit</th>
            <th>Delete</th>
          </tr>
        </thead>
        <tbody>
          {/* {<tr>
            <td>John</td>
            <td>Doe</td>
            <td>john@example.com</td>
          </tr>} */}
          {todos.map((todo) => (
            <tr key={todo.todoid}>
              <td>{todo.description}</td>
              <td><EditTodo todo={todo}/></td>
              <td
                className="btn btn-danger my-2"
                onClick={() => deleteTodo(todo.todoid)}
              >
                Delete
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </Fragment>
  );
}
