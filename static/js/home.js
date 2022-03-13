// siginin

function checkSignin(){
    let dialogue = document.getElementById('loginDialogue')
    dialogue.style.display = "block";
    let signinBox = document.getElementById('sigininMod')
    signinBox.style.display = "block";
    document.body.style.overflow = 'hidden';
}

function closeSignin() {
    let dialogue = document.getElementById('loginDialogue')
    dialogue.style.display = "none";
    let signinBox = document.getElementById('sigininMod')
    signinBox.style.display = "none";
    document.body.style.overflow = 'scroll';
}

// signup

function checkSignup(){
    let dialogue = document.getElementById('signupDialogue')
    dialogue.style.display = "block";
    let signupBox = document.getElementById('sigupMod')
    signupBox.style.display = "block";
    document.body.style.overflow = 'hidden';
}

function closeSignup() {
    let dialogue = document.getElementById('signupDialogue')
    dialogue.style.display = "none";
    let signupBox = document.getElementById('sigupMod')
    signupBox.style.display = "none";
    document.body.style.overflow = 'scroll';

}
