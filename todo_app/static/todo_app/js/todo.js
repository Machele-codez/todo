// getting all the present tasks into one array
const 
tasks = document.querySelectorAll('.item'),
duplicateError = document.querySelector('.duplicate-error-msg');
addTaskButton = document.querySelector('button[type="submit"]');

let presentTasks = [];

tasks.forEach(elem => {
    presentTasks.push(elem.textContent.trim().toLowerCase());
});

// adding onfocus listener to the input to check if the input is already a present task
let input = document.querySelector('input[name="text"]');
const h = addTaskButton.style.height;

input.onkeyup = () => {
    duplicateError.hidden = false
    addTaskButton.style.height = h;
    if (presentTasks.includes(input.value.trim().toLowerCase())) {
        duplicateError.classList.remove('alright');
        duplicateError.classList.add('already-present');
        duplicateError.innerHTML = 'Task already present';
    } else {
        duplicateError.classList.remove('already-present');
        duplicateError.classList.add('alright');
        duplicateError.innerHTML = 'Can be added';
    }
}


input.onblur = () => {
    duplicateError.hidden = true
}
