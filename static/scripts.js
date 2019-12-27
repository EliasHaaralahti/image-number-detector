$('.loader').hide();
$('#percentages-table').hide();

context = document.getElementById('canvas').getContext("2d");

var clickX = new Array();
var clickY = new Array();
var clickDrag = new Array();
var paint;

// White background for image processing.
context.fillStyle = "white";
context.fillRect(0, 0, context.canvas.width, context.canvas.height)

function redraw() {
	context.clearRect(0, 0, context.canvas.width,
				context.canvas.height);

	context.fillStyle = "white";
	context.fillRect(0, 0, context.canvas.width,
				context.canvas.height)

	context.strokeStyle = "#000000";
	context.lineJoin = "round";
	context.lineWidth = 10;

	for (var i = 0; i < clickX.length; i++) {
		context.beginPath();
		if (clickDrag[i] && i) {
			context.moveTo(clickX[i-1], clickY[i-1]);
		} else {
			context.moveTo(clickX[i]-1, clickY[i]);
		}
		context.lineTo(clickX[i], clickY[i]);
		context.closePath();
		context.stroke();
	}
}

function addClick(x, y, dragging) {
	clickX.push(x);
	clickY.push(y);
	clickDrag.push(dragging);
}

$('#clearCanvas').mousedown( function(e) {
	clickX = new Array();
	clickY = new Array();
	clickDrag = new Array();

	context.clearRect(0, 0, context.canvas.width,
				context.canvas.height);
	setResult("");
});

function setResult(result) {
	if (result == "") {
		$('#result').text("");
	} else {
		// TODO: Do something with results.raw 
		// (contains 10 values that are percentages 
		// of prediction)
		$('#result').text("The number appears to be: " + result.prediction);

		for (let i = 0; i < 10; i++) {
			const probability = (parseFloat(result.raw[i]) * 100).toFixed(2);
			$('#' + i).text( probability + "%" );
		}

		$('#percentages-table').show();
	}
}

$('#submitCanvas').mousedown( function(e) {
	var dataURL = canvas.toDataURL();

	$.ajax({
		type: "POST",
		url: "/result",
		data: { imageBase64: dataURL },
		success: function(data) {
			setResult(data);
		},
		beforeSend: function() {
			$('.loader').show();
		},
		complete: function() {
			$('.loader').hide();
		}
	});
});

$('#canvas').mousedown( function(e) {
	var mouseX = e.pageX - this.offsetLeft;
	var mouseY = e.pageY - this.offsetTop;

	paint = true;
	addClick(e.pageX - this.offsetLeft, e.pageY - this.offsetTop);
	redraw();
});

$('#canvas').mousemove( function(e) {
	if (paint) {
		addClick(e.pageX - this.offsetLeft,
			e.pageY - this.offsetTop,
			true);
		redraw();
	}
});

$('#canvas').mouseup( function(e) {
	paint = false;
});

$('#canvas').mouseleave(function(e) {
	paint = false;
});
