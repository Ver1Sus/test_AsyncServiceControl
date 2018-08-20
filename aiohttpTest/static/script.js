
var socket = new WebSocket("ws://5.166.41.52:50001/ws");


function sendToServer(msg){
	socket.send(msg);
	console.log(msg);
}


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
		//--- Send on websocket to update DB
		var msg = $("#checkActive").prop('checked');
		sendToServer(msg);
		changeButtons();
	});
	
	
  };






