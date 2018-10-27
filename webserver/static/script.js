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
	
	fetch('/logs', {'credentials': 'include'})
		.then(response => response.json())
		.then(logsJson => ractive.set('logs', logsJson._default));

}, false);
