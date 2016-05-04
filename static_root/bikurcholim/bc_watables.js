$(document).ready( function() {
        //An example with all options.
         var waTable = $('#div1').WATable({
            debug:true,                 //Prints some debug info to console
            pageSize: 10,                //Initial pagesize
            //transition: 'slide',       //Type of transition when paging (bounce, fade, flip, rotate, scroll, slide).Requires https://github.com/daneden/animate.css.
            //transitionDuration: 0.2,    //Duration of transition in seconds.
            filter: true,               //Show filter fields
            sorting: true,              //Enable sorting
            sortEmptyLast:true,         //Empty values will be shown last
            columnPicker: true,         //Show the columnPicker button
            pageSizes: [5,10,50,100,'All'],  //Set custom pageSizes. Leave empty array to hide button.
            hidePagerOnEmpty: true,     //Removes the pager if data is empty.
            checkboxes: true,           //Make rows checkable. (Note. You need a column with the 'unique' property)
            checkAllToggle:true,        //Show the check-all toggle
            preFill: true,              //Initially fills the table with empty rows (as many as the pagesize).
            //url: '/someWebservice'    //Url to a webservice if not setting data manually as we do in this example
            //urlData: { report:1 }     //Any data you need to pass to the webservice
            //urlPost: true             //Use POST httpmethod to webservice. Default is GET.
            types: {                    //Following are some specific properties related to the data types
                string: {
                   //filterTooltip: "Click here to sort..."    //What to say in tooltip when hoovering filter fields. Set false to remove.
                   placeHolder: "Type here..."    //What to say in placeholder filter fields. Set false for empty.
                },
                number: {
                    decimals: 2   //Sets decimal precision for float types
                },
                bool: {
                    //filterTooltip: false
                },
                date: {
                  utc: true,            //Show time as universal time, ie without timezones.
                  format: 'yyyy-MM-dd',   //The format. See all possible formats here http://arshaw.com/xdate/#Formatting.
                  datePicker: true      //Requires "Datepicker for Bootstrap" plugin (http://www.eyecon.ro/bootstrap-datepicker).
                }
            },
            actions: {                //This generates a button where you can add elements.
                filter: true,         //If true, the filter fields can be toggled visible and hidden.
                columnPicker: true,   //if true, the columnPicker can be toggled visible and hidden.
                custom: [             //Add any other elements here. Here is a refresh and export example.
                  $('<a href="#" class="refresh"><span class="glyphicon glyphicon-refresh"></span>&nbsp;Refresh</a>'),
                  $('<a href="#" class="export_all"><span class="glyphicon glyphicon-share"></span>&nbsp;Export all data</a>'),
                  $('<a href="#" class="export_checked"><span class="glyphicon glyphicon-share"></span>&nbsp;Export checked rows</a>'),
                  $('<a href="#" class="export_filtered"><span class="glyphicon glyphicon-share"></span>&nbsp;Export filtered data</a>'),
                  $('<a href="#" class="advanced"><span class="glyphicon glyphicon-share"></span>&nbsp;Advanced Pivot</a>')
                ]
            },
            tableCreated: function(data) {    //Fires when the table is created / recreated. Use it if you want to manipulate the table in any way.
                console.log('table created'); //data.table holds the html table element.
                console.log(data);            //'this' keyword also holds the html table element.
            },
            rowClicked: function(data) {      //Fires when a row is clicked (Note. You need a column with the 'unique' property).
                console.log('row clicked');   //data.event holds the original jQuery event.
                console.log(data);            //data.row holds the underlying row you supplied.
                                              //data.column holds the underlying column you supplied.
                                              //data.checked is true if row is checked.
                                              //'this' keyword holds the clicked element.
            },
            columnClicked: function(data) {    //Fires when a column is clicked
              console.log('column clicked');  //data.event holds the original jQuery event
              console.log(data);              //data.column holds the underlying column you supplied
                                              //data.descending is true when sorted descending (duh)
            },
            pageChanged: function(data) {      //Fires when manually changing page
              console.log('page changed');    //data.event holds the original jQuery event
              console.log(data);              //data.page holds the new page index
            },
            pageSizeChanged: function(data) {  //Fires when manually changing pagesize
              console.log('pagesize changed');//data.event holds teh original event
              console.log(data);              //data.pageSize holds the new pagesize
            }
        }).data('WATable');  //This step reaches into the html data property to get the actual WATable object. Important if you want a reference to it as we want here.

        //Generate some data
        var data = getData();
		
        waTable.setData(data);  //Sets the data.
        //waTable.setData(data, true); //Sets the data but prevents any previously set columns from being overwritten
        //waTable.setData(data, false, false); //Sets the data and prevents any previously checked rows from being reset

        var allRows = waTable.getData(false); //Gets the data you previously set.
        var checkedRows = waTable.getData(true); //Gets the data you previously set, but with checked rows only.
        var filteredRows = waTable.getData(false, true); //Gets the data you previously set, but with filtered rows only.

        var pageSize = waTable.option("pageSize"); //Get option
        //waTable.option("pageSize", pageSize); //Set option

        //Example event handler triggered by the custom refresh link above.
        $('body').on('click', '.refresh', function(e) {
            e.preventDefault();
            var data = getData();
            waTable.setData(data, true);
        });
        //Example event handler triggered by the custom export links above.
        $('body').on('click', '.export_checked, .export_filtered, .export_all, .advanced', function(e) {
            e.preventDefault();
            var elem = $(e.target);
            var data;
            if (elem.hasClass('export_all')) {
				data = waTable.getData(false, true);
				download(JSON.stringify(data), waTable.getAllCols(), '/bikurcholim/export_xls/')
			}
            else if (elem.hasClass('export_checked')) {
            	data = waTable.getData(true);
            	download(JSON.stringify(data), waTable.getCheckedCols(), '/bikurcholim/export_xls/')
            }
            else if (elem.hasClass('export_filtered')) {
            	data = waTable.getData(false, true);
				download(JSON.stringify(data), waTable.getCheckedCols(), '/bikurcholim/export_xls/')
            }
            else if (elem.hasClass('advanced')) {
            	data = waTable.getData(false, true);
				download(JSON.stringify(data), waTable.getCheckedCols(), '/bikurcholim/'+smallName+'_advanced/')
            }
            console.log(data.rows.length + ' rows returned');
            console.log(data);
            
        });
		

		function download(data, checkedCols, page){
			// Build a form
			var form = $('<form></form>').attr('action', page).attr('method', 'post');
			form.append($('<input></input>').attr('type', 'hidden').attr('name', 'csrfmiddlewaretoken').attr('value', csrftoken));
			// Add the one key/value
			form.append($("<input></input>").attr('type', 'hidden').attr('name', 'data').attr('value', data));
			form.append($("<input></input>").attr('type', 'hidden').attr('name', 'checkedCols').attr('value', checkedCols));
			//send request
			form.appendTo('body').submit().remove();
		};
		
		function getCookie(name) {
			var cookieValue = null;
			if (document.cookie && document.cookie != '') {
				var cookies = document.cookie.split(';');
				for (var i = 0; i < cookies.length; i++) {
					var cookie = jQuery.trim(cookies[i]);
					// Does this cookie string begin with the name we want?
					if (cookie.substring(0, name.length + 1) == (name + '=')) {
						cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
						break;
					}
				}
			}
			return cookieValue;
		}
		var csrftoken = getCookie('csrftoken');

    });
	function getData() {
		var json = json_data;
		json=json.replace(/&quot;/g, '"');
		json=json.replace(/&lt;/g, '<');
		json=json.replace(/&gt;/g, '>');
		json=json.replace(/&#39;/g, "'");
		json=json.replace(/(\r\n|\n|\r)/gm," ");
		obj = JSON.parse(json);
		var data = {
            cols: obj.cols,
            rows: obj.rows,
        };
		return data;
	}