import React, { Fragment, useState } from "react";

export default function InputTodo() {
  const [description, setDescription] = useState("");

  const onSubmitForm = async(e) => {
    e.preventDefault();
    try {
        const body = {description};
        const response = await fetch("http://localhost:5000/todos",{
            method : "POST",
            headers : {"Content-type": "application/json"},
            body: JSON.stringify(body)
        });
        window.location = "/";
    } catch (err) {
        console.error(err.message)
    }
  };
  
  return (
    <Fragment>
      <h1 className="text-center mt-5">PERN Stack Todo List</h1>
      <form className="d-flex mt-5" onSubmit={onSubmitForm}>
        <input
          type="text"
          className="form-control mr-2"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          placeholder="Write the task to add.."
          required
        />
        <button className="btn btn-success p-3">Add</button>
      </form>
    </Fragment>
  );
}
