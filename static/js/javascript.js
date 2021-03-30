
function addElement(n) {
    var expresion = document.getElementById("expresion").value;
    document.getElementById("expresion").value = expresion + n;
}

function popElement() {
    var expresion = document.getElementById("expresion").value;

    // Quitamos los sin¹, cos¹, tan¹
    if(expresion.slice(-1) == '¹'){
        document.getElementById("expresion").value = expresion.slice(0,-4);
    }
    // Quitamos los sin, cos y tan
    else if(expresion.slice(-1) == 'n' || expresion.slice(-1) == 's'){
        document.getElementById("expresion").value = expresion.slice(0,-3);
    }
    else {
        document.getElementById("expresion").value = expresion.slice(0,-1);
    }
}

function erase() {
    document.getElementById("expresion").value = "";
}