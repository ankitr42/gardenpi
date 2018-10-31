document.addEventListener('DOMContentLoaded', function() {
    var ractive = new Ractive({
	  target: '#logs-div',
	  template: '#logs-template',
	  data: { 
				formatEpoch: function(epoch) {
					var epochDate = new Date(0);
					epochDate.setUTCSeconds(epoch);
					return epochDate.toLocaleString();
				}
			}
	});
	
	updateLogs = function() {
		fetch('/logs', {'credentials': 'include'})
		.then(response => response.json())
		.then(logsJson => ractive.set('logs', logsJson._default));
		
		setTimeout(updateLogs, 30000);
	}
	
	updateLogs();
	
	window.startFeed = function() {
		var feedFrame = document.createElement('iframe');
		
		feedFrame.src = 'http://waterpi.ddns.net:81/mjpeg';
		feedFrame.style = 'width:640px; height: 480px'
		document.getElementById('live-feed').appendChild(feedFrame);
	}

}, false);
