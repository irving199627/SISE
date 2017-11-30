with(document.registro){
	onsubmit = function(e){
    var expreg = new RegExp(/^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$/);
		e.preventDefault();
		ok = true;
		if(ok && first_name.value==""){
			ok=false;
			alert("Debe escribir SU NOMBRE");
			first_name.focus();
		}
    if(ok && last_name.value==""){
			ok=false;
			alert("Debe escribir SU APELLIDO");
			last_name.focus();
		}
    if(ok && username.value==""){
			ok=false;
			alert("Debe escribir SU NOMBRE DE USUARIO");
			username.focus();
		}
    if(ok && email.value==""){
			ok=false;
			alert("Debe escribir SU EMAIL");
			email.focus();
		}
    if(ok && password1.value==""){
			ok=false;
			alert("Debe escribir SU CONTRASEÑA");
			password1.focus();
		}
    if(ok && password1.value != password2.value){
      ok = false;
      alert("Las contraseñas no coinciden")
      password2.focus();
    }
    if (ok &&  expreg.test(password1.value)) {
    }else{
      ok = false;
      alert("La contraseña debe contener al menos una letra Mayuscula, una minuscula, un digito y debe tener entre 8 y 16 caracteres")
      password1.focus();
    }

    if(ok){ submit(); }
	}
}
