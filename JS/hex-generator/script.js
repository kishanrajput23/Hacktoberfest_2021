// generate color
function getColor() {
	return '#' + Math.random().toString(16).slice(2, 8);
}
// set background color style
function setBackground() {
	var bgColor = getColor();
	document.body.style.background = bgColor;
	document.getElementById("hex").innerHTML = bgColor;
}
// change color on spacebar press 
document.body.onkeyup = function(e) {
	if (e.keyCode == 32) {
		setBackground();
	}
};
// change color on mouse click
$(function() {
	$(document).on('click', function(e) {
		if (e.target.className === 'btn') {
			$('#success').css('display', '');
			$('#success').fadeOut(2000);
            $('button').blur()
			document.getSelection().removeAllRanges();
		} else {
			setBackground();
		}
	});
});

// clipboard button
var clipboard = new Clipboard('.btn');

