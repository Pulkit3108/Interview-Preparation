# Node.js

Node.js asynchronous programming, streams, Express, and data access.

[Back to the question-bank index](../README.md)

## How to handle promises in Node.js?

**Answer**

.then() and .catch(): Handle resolved values and errors of promises.
async and await: Provide a more readable way to work with promises, making asynchronous code look synchronous.
Promise.all: Handle multiple promises concurrently, resolving when all promises resolve or rejecting if any promise rejects.
Promise.race: Resolve or reject as soon as one of the promises resolves or rejects.
Promise.allSettled: Resolve after all promises have either resolved or rejected, providing the outcome of each promise

## What are streams in Node.js?

**Answer**

Streams in Node.js are objects that allow you to read data from a source or write data to a destination in a continuous fashion. They are particularly useful for handling large amounts of data or working with data that is being generated or received over time, such as reading files, handling HTTP requests, or processing data from a network.
Types of Streams in Node.js
Readable Streams: Streams from which data can be read (e.g., fs.createReadStream).
Writable Streams: Streams to which data can be written (e.g., fs.createWriteStream).
Duplex Streams: Streams that are both readable and writable (e.g., TCP sockets).
Transform Streams: Duplex streams that can modify or transform the data as it is written and read (e.g., zlib.createGzip).

## Tell a bit about express in node js

**Answer**

Express: A minimal and flexible web application framework for Node.js that provides a robust set of features for building web and mobile applications.
Key Features:
Routing: Define routes for different HTTP methods and URL patterns.
Middleware: Use middleware functions for tasks such as logging, authentication, and parsing request bodies.
Template Engines: Generate HTML dynamically using template engines like Pug, EJS, and Handlebars.
Static Files: Serve static files such as images, CSS files, and JavaScript files.
Error Handling: Handle errors consistently in your application.
Extensibility: Integrate middleware and plugins to add functionality.

## How will you connect with DB?

**Answer**

Set Up the Project:
Install Node.js and initialize a new Node.js project.
Install required packages (Express, body-parser, database client).
Set Up Express.js:
Create the main application file and set up a basic Express server.
Connect to the Database:
For MongoDB, use Mongoose to connect to the database.
For PostgreSQL, use Sequelize to connect to the database.
Define Models and Routes:

**Define models for your data.**

Create routes to handle API endpoints.
Use the routes in the main application file.
