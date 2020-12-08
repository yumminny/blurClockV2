var socket;

function setup() {

  	console.log('trying to connect to socket');
	socket = io();
	socket.on('zipResult', showAPIData)


	output = createElement('h2', '');
	output.position(20, 70);

	document.querySelector("#submit").onclick = () => {
		sendRequest();
	}	

	document.querySelector("#startBlurClock").onclick = () => {
		console.log('start blur clock');
		socket.emit('startBlurClock');
	}

	document.querySelector("#endBlurClock").onclick = () => {
		console.log('end blur clock');
		socket.emit('endBlurClock');
	}

	document.querySelector("#startSunClock").onclick = () => {
		socket.emit('startSunClock');
		console.log('start sun clock')
	}

	document.querySelector("#endSunClock").onclick = () => {
		socket.emit('endSunClock');
		console.log('end sun clock')
	}

	document.querySelector("#runClock").onclick = () => {
		console.log('turning on clock');
		socket.emit('runClock');
	}

	document.querySelector("#killClock").onclick = () => {
		console.log('turning off clock');
		socket.emit('killClock');
	}

	document.querySelector("#moveMotorForward").onclick = () => {
		console.log('motor forward call');
		socket.emit('moveMotorForward');
	}

	document.querySelector("#moveMotorBackward").onclick = () => {
		console.log('motor backwards call');
		socket.emit('moveMotorBackward');
	}
}

function sendRequest(){

	const zipIn = document.getElementById('zipInput').value
	var data = {
		zip : zipIn
	}
	socket.emit('getZipData',data);
}


function showAPIData(data){
	console.log('got results: '+data.sunRise);
	// output.html('Got Result: <br/> Location:'+data.city+'</br>Sunrise:'+data.sunRise+'<br/>Sunset:'+data.sunSet);
	document.querySelector("#zipOutput").textContent  = 'Got Result:</br> Location:'+data.city+'</br>Sunrise:'+data.sunRise+'<br/>Sunset:'+data.sunSet
}
