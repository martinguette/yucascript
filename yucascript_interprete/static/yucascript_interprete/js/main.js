document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var options = {}
    var instances = M.Sidenav.init(elems, options);
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, options);
});
function verificar(){
    var data = editor.getDoc().getValue()
    console.log(data)
    $.ajax({
        url: 'http://127.0.0.1:3200/interprete/validar',
        dataType: 'text',
        type: 'post',
        contentType: 'application/json',
        data: data,
        success: function(data){
            console.log(data)
        },
        error: function(){
            console.log("e")
        }
    })
    /*var xhr = new XMLHttpRequest();
    xhr.open('POST', "http://127.0.0.1:8000/interprete/validar", true);
    xhr.send();
    xhr.onreadystatechange = function(e){
        console.log(e)
    }*/
}
var editor = CodeMirror(document.getElementById("editor"), {
    lineNumbers: true,
    theme: "yonce"
});
document.getElementById('archivo').addEventListener('change', getFile)
function getFile(event) {
    const input = event.target
    M.Modal.getInstance(document.getElementById("modal1")).close()
    console.log(input.files[0])
    if (input.files[0].name.split('.').pop() == "yuca"){
        if ('files' in input && input.files.length > 0) {
        console.log("a")
        placeFileContent(
        document.getElementById('content-target'),
        input.files[0])
        }
        input.value =""
    }else{
        M.Modal.getInstance(document.getElementById("modal2")).open()
    }
    
}
function placeFileContent(target, file) {
    readFileContent(file).then(content => {
    //target.value = content
    editor.getDoc().setValue(content)
    console.log(document.getElementById("editor"))
    }).catch(error => console.log(error))
    }
function readFileContent(file) {
    const reader = new FileReader()
    return new Promise((resolve, reject) => {
        reader.onload = event => resolve(event.target.result)
        reader.onerror = error => reject(error)
        reader.readAsText(file)
    })
}