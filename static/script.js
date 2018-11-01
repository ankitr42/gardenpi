document.addEventListener('DOMContentLoaded', function() {
    var pumpRactive = new Ractive({
	  target: '#pump-logs-div',
	  template: '#pump-logs-template',
	  data: { 
				formatEpoch: function(epoch) {
					var epochDate = new Date(0);
					epochDate.setUTCSeconds(epoch);
					return epochDate.toLocaleString();
				}
			}
	});
	
	var fanRactive = new Ractive({
	  target: '#thermal-logs-div',
	  template: '#thermal-logs-template',
	  data: { 
				formatEpoch: function(epoch) {
					var epochDate = new Date(0);
					epochDate.setUTCSeconds(epoch);
					return epochDate.toLocaleString();
				}
			}
	});
	
	var chargeRactive = new Ractive({
	  target: '#charge-logs-div',
	  template: '#charge-logs-template',
	  data: { 
				formatEpoch: function(epoch) {
					var epochDate = new Date(0);
					epochDate.setUTCSeconds(epoch);
					return epochDate.toLocaleString();
				}
			}
	});
	
	updatePumpLogs = function() {
		fetch('/logs/pump/', {'credentials': 'include'})
		.then(response => response.json())
		.then(logsJson => pumpRactive.set('logs', logsJson));
		
		setTimeout(updatePumpLogs, 30*1000);
	}
	
	updateChargeLogs = function() {
		fetch('/logs/charge/', {'credentials': 'include'})
		.then(response => response.json())
		.then(logsJson => chargeRactive.set('logs', logsJson));
		
		setTimeout(updateChargeLogs, 600*1000);
	}
	
	updateThermalLogs = function() {
		fetch('/logs/thermal/', {'credentials': 'include'})
		.then(response => response.json())
		.then(logsJson => fanRactive.set('logs', logsJson));
		
		setTimeout(updateThermalLogs, 30*1000);
	}
	
	updatePumpLogs();
	updateChargeLogs();
	updateThermalLogs();
	
	pumpRactive.set('fullLogs', '/logs/pump/all');
	chargeRactive.set('fullLogs', '/logs/charge/all');
	fanRactive.set('fullLogs', '/logs/thermal/all');
	
	window.startFeed = function() {
		var feedFrame = document.createElement('iframe');
		
		feedFrame.src = 'http://waterpi.ddns.net:81/mjpeg';
		feedFrame.style = 'width:640px; height: 480px'
		document.getElementById('live-feed').appendChild(feedFrame);
	}

}, false);
