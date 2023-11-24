// Define the base URL for the API
const apiUrl = "http://127.0.0.1:4558/";

// Function to load all tasks from the server
async function loadTasks() {
  fetch(`${apiUrl}/tasks`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    },
  })
    .then(response => response.json())
    .then(data => {
      console.log(data);
      // Add each task to the task list
      const taskList = document.getElementById('task-list');
      taskList.innerHTML = ""
      for (const taskId in data) {
        const task = data[taskId];
        let newTask = createTaskElement(task.title, task.description, task.due_date, task.completed, taskId);

        // const newTask = document.createElement("li");
        // newTask.classList.add('list-group-item', 'd-flex', 'justify-content-between', 'align-items-center');
        // newTask.innerHTML = `Title:${task.title}, Desc:${task.description}, Completed:${task.completed} 
        //       <div>
        //           <button class="btn btn-sm btn-success mr-2" onclick="completeTask(${taskId})">Complete</button>
        //           <button class="btn btn-sm btn-danger" onclick="deleteTask(${taskId})">Delete</button>
        //       </div>`;
        taskList.appendChild(newTask);
      }
    })
    .catch(error => console.error('Error:', error));
}

// Function to update a task
async function completeTask(taskId, title, description, due_date) {
  const task = {
    title: title,
    description: description,
    due_date: due_date,
    completed: true
  };
  // Make the API request to update the task
  const response = await fetch(`${apiUrl}/tasks/${taskId}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(task),
  });

  // Parse the response body as JSON
  const responseBody = await response.json();

  loadTasks();

  // Log the response for debugging purposes
  console.log(responseBody);
}

// Function to delete a task
async function deleteTask(taskId) {
  // Make the API request to delete the task
  const response = await fetch(`${apiUrl}/tasks/${taskId}`, {
    method: "DELETE",
  });

  // Parse the response body as JSON
  const responseBody = await response.json();

  loadTasks();

  // Log the response for debugging purposes
  console.log(responseBody);
}

// Load all tasks when the page is loaded
loadTasks();

window.addEventListener("DOMContentLoaded", (event) => {
  const createTaskForm = document.querySelector('#create-task-form');
  // Get references to the HTML elements we need
  // const taskForm = document.getElementById("task-form");
  const taskTitleInput = document.getElementById("title");
  const taskDescriptionInput = document.getElementById("description");
  const taskDueDateInput = document.getElementById("due_date");
  const taskList = document.getElementById("task-list");

  if (createTaskForm) {
    createTaskForm.addEventListener("submit", createTask);
  }

  if (createTaskForm) {
    createTaskForm.addEventListener("submit", createTask);
  }

  if (createTaskForm) {
    createTaskForm.addEventListener("submit", createTask);
  }

  if (createTaskForm) {
    createTaskForm.addEventListener("submit", createTask);
  }

  // Function to create a new task
  async function createTask(event) {
    // Prevent the default form submission behavior
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    // Build the request body
    const task = {
      title: taskTitleInput.value,
      description: taskDescriptionInput.value,
      due_date: taskDueDateInput.value,
      completed: false
    };

    // Make the API request to create the new task
    fetch(`${apiUrl}/tasks`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(task)
    })
      // Parse the response body as JSON
      .then(response => response.json())
      // Add the new task to the task list
      .then(data => {
        loadTasks();
        // Clear the form inputs
        taskTitleInput.value = "";
        taskDescriptionInput.value = "";
        taskDueDateInput.value = "";
      })
      .catch(error => console.error('Error:', error));
  }
});

// Function to create new task element
function createTaskElement(title, description, due_date, completed, id) {
  // Create a new list item
  let listItem = document.createElement('li');
  listItem.className = 'list-group-item d-flex justify-content-between align-items-center';

  // Create the task title element
  let taskTitle = document.createTextNode(title);

  // Create the task description element
  let taskDescription = document.createElement('small');
  taskDescription.className = 'text-muted ml-2';
  taskDescription.innerText = description;

  // Create the task due date element
  let taskDueDate = document.createElement('small');
  taskDueDate.className = 'text-muted ml-2';
  taskDueDate.innerText = due_date;

  // Create the complete button element
  let completeButton = document.createElement('button');
  completeButton.className = 'btn btn-sm btn-success mr-2';
  completeButton.innerText = 'Complete';
  completeButton.addEventListener('click', function () {
    completeTask(id, title, description, due_date);
  });

  // Create the delete button element
  let deleteButton = document.createElement('button');
  deleteButton.className = 'btn btn-sm btn-danger';
  deleteButton.innerText = 'Delete';
  deleteButton.addEventListener('click', function () {
    deleteTask(id);
  });

  // Add the task title, description, due date, complete button, and delete button elements to the list item
  listItem.appendChild(taskTitle);
  listItem.appendChild(taskDescription);
  listItem.appendChild(taskDueDate);
  if (!completed) {
    listItem.appendChild(completeButton);
  }
  listItem.appendChild(deleteButton);
 

  // Return the list item element
  return listItem;
}