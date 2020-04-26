//| getting all the present tasks into one array
const 
taskTexts = document.querySelectorAll('.task-text'),
duplicateError = document.querySelector('.duplicate-error-msg');
addTaskButton = document.querySelector('button[type="submit"]');
taskPriority = document.querySelectorAll('.task-priority')
//| getting all present taskTexts, well formatted
let presentTasks = [];
taskTexts.forEach(elem => {
    presentTasks.push(elem.textContent.trim().toLowerCase());
});

//| adding onfocus listener to the input to check if the input is already a present task
let input = document.querySelector('input[name="text"]');
const h = addTaskButton.style.height;

input.addEventListener('keyup', () => {
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
});

//| Display duplicate alert upon attempt to submit
addTaskButton.addEventListener('click', e => {
    if (presentTasks.includes(input.value.trim().toLowerCase())) {
        e.preventDefault();
        document.getElementById('duplicate-alert').hidden = false
    }
})

//| dismiss alert
document.getElementById('duplicate-alert-dismiss').addEventListener('click', () =>{
    document.getElementById('duplicate-alert').hidden = true;    
})


//| clear duplicate error message when input is not active
input.addEventListener('blur', () => {
    duplicateError.hidden = true
});

//| left edge colour based on task priority 
document.querySelectorAll('.A').forEach(elem => {
    elem.style.backgroundColor = 'red'
});
document.querySelectorAll('.B').forEach(elem => {
    elem.style.backgroundColor = 'orange'
});
document.querySelectorAll('.C').forEach(elem => {
    elem.style.backgroundColor = '#ffef00'
});
document.querySelectorAll('.D').forEach(elem => {
    elem.style.backgroundColor = 'gray'
});

//| placeholder for `set priority`
document.querySelector('option[selected]').innerHTML = 'set priority';

//| form errors
const fieldErrorDismiss = document.querySelector('.field-errors-close');
fieldErrorDismiss.addEventListener('click', () => {
    document.querySelector('.field-errors').style.display = 'none';
})
