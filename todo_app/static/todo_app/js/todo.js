//| getting all the present tasks into one array
const 
tasks = document.querySelectorAll('.item'),
duplicateError = document.querySelector('.duplicate-error-msg');
addTaskButton = document.querySelector('button[type="submit"]');

//| getting all present tasks, well formatted
let presentTasks = [];
tasks.forEach(elem => {
    presentTasks.push(elem.textContent.trim().toLowerCase());
});

//| adding onfocus listener to the input to check if the input is already a present task
let input = document.querySelector('input[name="text"]');
const h = addTaskButton.style.height;

input.onkeyup = () => {
    duplicateError.hidden = false
    addTaskButton.style.height = h; //? maintain add task button's height when error message is added below input
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

//| handle task duplicate error, by preventing form submission if tasks wants to be duplicated
addTaskButton.onclick = (e) => {
    if (presentTasks.includes(input.value.trim().toLowerCase())){
        e.preventDefault();
        document.getElementById('duplicate-alert').hidden = false;
    }
}

//| clear duplicate error message when input is not active
input.onblur = () => {
    duplicateError.hidden = true
}
