function empty(){
	var x = document.getElementById("must-field").value;
	console.log(x);
	if (x == ''){
		alert("Oops field is empty!");
		return false;
	};
}
