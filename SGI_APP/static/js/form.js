// Object Javascript
const validator = {
    isEmpty: (value) => value === undefined || value.trim() === "",
    isEmptyU: (value) => value === undefined,
    isEmptyS: (value) => value.trim() === "",
    isEqual: (v1, v2) => v1 === v2,
};

function validate() {
    let usuario = $("#usuario").val();
    let pasw = $("#password").val();

    document.getElementById("usuario-label").classList.remove("error")
    document.getElementById("password-label").classList.remove("error")

    if (validator.isEmpty(usuario) || validator.isEmpty(pasw)) {
        document.getElementById("empty-user-pasw").classList.add("display", "error")
        document.getElementById("empty-user-pasw").classList.remove("non-display")
        if (validator.isEmpty(usuario)) {
            document.getElementById("usuario-label").classList.add("error")
        }
        if (validator.isEmpty(pasw)) {
            document.getElementById("password-label").classList.add("error")
        }
        return false;
    }
    return true;
}

function active (id){
    document.getElementById(id).classList.add("active")
}

function desactive(id){
    let id1 = "#" + id
    let campo = $(id1).val()
    if(validator.isEmpty(campo)){
        document.getElementById(id + "-label").classList.remove("active")
    }
}

function update(){
    let usuario = $("#usuario").val()
    let password = $("#password").val()

    if(!validator.isEmpty(usuario)){
        document.getElementById("usuario-label").classList.add("active")
    }else{
         document.getElementById("usuario-label").classList.remove("active")
    }
    if(!validator.isEmpty((password))){
        document.getElementById("password-label").classList.add("active")
    }else{
         document.getElementById("password-label").classList.remove("active")
    }

}

(function () {
    $(document).ready(function () {
        var toastTrigger = document.getElementById('liveToastBtn')
        var toastLiveExample = document.getElementById('liveToast')
        if (toastTrigger) {
            toastTrigger.addEventListener('click', function () {
                var toast = new bootstrap.Toast(toastLiveExample)

                toast.show()
            })
        }
    });
})