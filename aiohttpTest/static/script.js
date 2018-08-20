
//var socket = io.connect('http://5.166.41.52:50001');
// var socket = new WebSocket("ws://5.166.41.52:50001/ws");

	//var pre = document.createElement("p"); 
	//pre.style.wordWrap = "break-word"; 
	//pre.innerHTML = "Connect"; 
	

/*
socket.onopen = function() {
  console.log("Соединение установлено.");
  
  $("input").on("click", function(e){
	// e.preventDefault(); //-- do not refresh page
	console.log("tests");
	// socket.send({
		// 'action' : this.value
		// });
		socket.send(this.value);
	});
	
	socket.onmessage = function(str) {
	  console.log("Someone sent: ", str);
	};
  
};
*/


function changeButtons(){
	if ($("#checkActive").prop('checked')){	
		$('button').prop('disabled', false);
		$('button').removeClass('btnDisabled');
	}
	else{
		$('button').prop('disabled', true);
		$('button').addClass('btnDisabled');
	}
}



window.onload = function() {
	//-------- disable/enable button
	changeButtons();
    $("#checkActive").change(function(){
		
		changeButtons();
	});
	
	
  };






