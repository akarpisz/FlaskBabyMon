$("button.btn#off").on("click", function(event){
	event.preventDefault();
	
	
	$.ajax("/api/off",
	{type: "POST"
	});
});

$("button#reboot").on("click", function(event){
		event.preventDefault();
		
		$.ajax("/api/reboot",
		{type: "POST"	
		});
});
