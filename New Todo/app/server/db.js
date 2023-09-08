const { Pool } = require('pg');
const fs = require('fs');

// Database connection configuration
const pool = new Pool({
  user: 'postgres',
  password: 'postgres',
  host: 'postgres',
  //port: 7000,
  //database: 'react_todo'
});


// SQL query to create the 'todo' table if it doesn't exist
const createTableQuery = `
  CREATE TABLE IF NOT EXISTS todo (
    todoid serial PRIMARY KEY,
    description VARCHAR(255)
  );
`;

// Function to create the 'todo' table
async function createTodoTable() {
  try {
    const client = await pool.connect();
    await client.query(createTableQuery);
    client.release();
    console.log('Table "todo" created or already exists.');
  } catch (error) {
    console.error('Error creating the table:', error);
  }
}

// Call the createTodoTable function when the Node.js application starts
createTodoTable();


// Export the pool for use in other parts of your application
module.exports = pool;

