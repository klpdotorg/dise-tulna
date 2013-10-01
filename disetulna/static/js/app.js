//Function to fill in the dropdowns and display the options
function change_focus(id,type,flag)
{
	var data='';
	var element=document.getElementById(type);
	if(type=='dise_blk')
		data=dise_block;
	else if(type=='dise_clust')
		data=dise_clust;
	else if(type=='klp_blk')
		data=klp_block;
	else if(type=='klp_clust')
		data=klp_clust;
	element.length=1;
	for(var i=0;i<data.length-1;i++){
		if(data[i][0]==id){
			if(flag==1)
				element.options[element.length]=new Option(data[i][2],data[i][1]);
			else{
				element.options[element.length]=new Option(data[i][1],data[i][1]);
			}
		}
	}
}
function filter(value){
	
  	var klptable = document.getElementById("klp-table");
	var disetable = document.getElementById("dise-table");
	var ele;
	
	
	for(var i=1;i<disetable.rows.length;i++){
		ele=disetable.rows[i].innerHTML.replace(/<[^>]+>/g,"|").split("|")[3];
		res=ele.toLowerCase().match(value.toLowerCase());
		if(res==value.toLowerCase()){
			disetable.rows[i].style.display='';
		}
		else{
			disetable.rows[i].style.display='none';
		}
	}

	for(var i=1;i<klptable.rows.length;i++){
		ele=klptable.rows[i].innerHTML.replace(/<[^>]+>/g,"|").split("|")[3];
		res=ele.toLowerCase().match(value.toLowerCase());
		if(res==value.toLowerCase()){
			klptable.rows[i].style.display='';
		}
		else{
			klptable.rows[i].style.display='none';
		}
	}
}


$('tr').click(function() {
	// $(this).addClass('warning').siblings().removeClass('warning');
	//console.log('meh');
});

//Function to replace unnecessary tags from the saved value
function replaceAll(txt, replace, with_this) {
  return txt.replace(new RegExp(replace,'g'),with_this);
}

var dise_value='';
var klp_value='';

//Storing the values clicked by the user from html
function register(value,type) {
			value_list= replaceAll(value.innerHTML,"<td>","");
			value_list= replaceAll(value_list,"</td>","|");
			value_list= value_list.substring(0,value_list.length-1);
			//value_list= value_list.split("|");
	if (type=='dise'){
			dise_value=value_list; 
			document.getElementById('dise_alert').innerHTML=dise_value.split("|")[1];
	} else {
			klp_value=value_list;
			document.getElementById('klp_alert').innerHTML=klp_value.split("|")[1];
	}
}

//Passing the selected values on button click save
function getdata() {
	var data = {'dise': dise_value, 'klp': klp_value, 'dise_clust':getURLParameter('dise'), 'klp_clust':getURLParameter('klp') };
	$.ajax({
	    type: "POST",
	    url: '/content',
	    data: data,
	    
	    success: function(response){ window.location=response; 
	    },
	    error: function (xhr, ajaxOptions, thrownError) {
          	alert(xhr.status);
        	alert(thrownError);
			alert("Error");
        }
	});
	
}

//Fetching the URL Parameters
function getURLParameter(name) {
  return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(location.search)||[,""])[1].replace(/\+/g, '%20'))||null
}