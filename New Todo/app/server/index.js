const express = require('express');
const app = express();
const port = 5000;
const cors = require('cors');
const pool = require("./db")

//MiddleWare
app.use(cors());
app.use(express.json());

//ROUTES

//create a todo 

app.post("/todos", async(req,res) => {
    try {
        const {description} = req.body
        const newTodo = await pool.query(
            "INSERT INTO todo (description) VALUES($1) RETURNING *",
            [description]
            );
        
        res.json(newTodo.rows[0]);
        
    } catch (err) {
        console.error(err.message);
    }
})

//get all todo

app.get("/todos", async(req,res) => {
    try {
        const allTodos = await pool.query("SELECT * FROM todo");
        res.json(allTodos.rows)
        
    } catch (err) {
        console.error(err.message);
        
    }
});

//get a todo
app.get("/todos/:id", async(req,res) => {
    try {
        const { id } = req.params;
        const todo = await pool.query("SELECT * FROM todo WHERE todoid = $1", [id]);
        res.json(todo.rows[0]);
    } catch (err) {
        console.error(err.message)
    }
});

//update a todo
app.put("/todos/:id", async(req,res) => {
    try {
        const { id } = req.params;
        const { description } = req.body;
        const updateTodo = await pool.query("UPDATE todo SET description = $1 WHERE todoid = $2", 
        [description, id]);
    } catch (err) {
        console.error(err.message);
    }
    res.json("Todo was updated")
});



//delete a todo
app.delete("/todos/:id", async(req,res) => {
    try {
        const {id} = req.params;
        const deleteTodo = await pool.query("DELETE FROM todo WHERE todoid = $1", [id]);
    } catch (err) {
        console.error(err.message);
    }
    res.json("Todo was deleted!")
});

//server start & message
app.listen(port, () => {
    console.log("The server has started on port 5000");
});

