	$(document).ready(function() {
		
		$('#calendar').fullCalendar({
			header: {
				left: 'prev,next today',
				center: 'title',
				right: 'month,agendaWeek,agendaDay'
			},
			defaultDate: today,
			defaultView: 'agendaDay',
			editable: false,
			eventLimit: true, // allow "more" link when too many events
			eventTextColor: 'white',
			events: {
		        url: events,
		        type: 'POST',
		        data: {
		            csrfmiddlewaretoken: csrftoken,
		            data_type: 'services'
		        },
		        error: function() {
					$('#script-warning').show();
				},
		   },
		   eventMouseover: function(calEvent, jsEvent) {
			    var tooltip = '<div class="tooltipevent" style="white-space: pre;width:150px;height:75px;background:#FFFFC8;position:absolute;z-index:10001;">' 
			    	+ 'Title: ' + calEvent.title + '\nStart: ' + new Date(calEvent.start).toLocaleDateString() + '\nEnd: ' 
			    	+ new Date(calEvent.end).toLocaleDateString() + '\nService: ' + calEvent.service + '</div>';
			    $("body").append(tooltip);
			    $(this).mouseover(function(e) {
			        $(this).css('z-index', 10000);
			        $('.tooltipevent').fadeIn('500');
			        $('.tooltipevent').fadeTo('10', 1.9);
			    }).mousemove(function(e) {
			        $('.tooltipevent').css('top', e.pageY + 10);
			        $('.tooltipevent').css('left', e.pageX + 20);
			    });
			},
			
			eventMouseout: function(calEvent, jsEvent) {
			    $(this).css('z-index', 8);
			    $('.tooltipevent').remove();
			},
		    dayClick: function(date, jsEvent, view) {
	                $('#calendar') 
	                   .fullCalendar('changeView', 'agendaDay'/* or 'basicDay' */);
	                $('#calendar') 
	                    .fullCalendar('gotoDate', date.format());

		    } 
		});
		$('#housingcalendar').fullCalendar({
			header: {
				left: 'prev,next today',
				center: 'title',
				right: 'month,agendaWeek,agendaDay'
			},
			defaultDate: today,
			defaultView: 'agendaWeek',
			editable: false,
			eventLimit: true, // allow "more" link when too many events
			eventTextColor: 'white',
			events: {
		        url: events,
		        type: 'POST',
		        data: {
		            csrfmiddlewaretoken: csrftoken,
		            data_type: 'housing'
		        },
		        error: function() {
					$('#script-warning').show();
				},
		        //color: 'yellow',   // a non-ajax option
		        //textColor: 'black' // a non-ajax option
		    },
			eventMouseover: function(calEvent, jsEvent) {
			    var tooltip = '<div class="tooltipevent" style="white-space: pre;width:150px;height:75px;background:#FFFFC8;position:absolute;z-index:10001;">' 
			    	+ 'Title: ' + calEvent.title + '\nStart: ' + new Date(calEvent.start).toLocaleDateString() + '\nEnd: ' 
			    	+ new Date(calEvent.end).toLocaleDateString() + '</div>';
			    $("body").append(tooltip);
			    $(this).mouseover(function(e) {
			        $(this).css('z-index', 10000);
			        $('.tooltipevent').fadeIn('500');
			        $('.tooltipevent').fadeTo('10', 1.9);
			    }).mousemove(function(e) {
			        $('.tooltipevent').css('top', e.pageY + 10);
			        $('.tooltipevent').css('left', e.pageX + 20);
			    });
			},
			
			eventMouseout: function(calEvent, jsEvent) {
			    $(this).css('z-index', 8);
			    $('.tooltipevent').remove();
			},
		    dayClick: function(date, jsEvent, view) {
	                $('#housingcalendar') 
	                   .fullCalendar('changeView', 'agendaDay'/* or 'basicDay' */);
	                $('#housingcalendar') 
	                    .fullCalendar('gotoDate', date.format());

		    },
			loading: function(bool) {
				$('#loading2').toggle(bool);
			}
		});
	});