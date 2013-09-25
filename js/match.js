function callpage(value){
	var dise=document.getElementById("dise_clust");
	var klp=document.getElementById("klp_clust");
	window.location.href="content/"+trim(dise.value)+"/"+trim(klp.value);
}

function getdata() {
	var dise=document.getElementById("dise_clust");
	var klp=document.getElementById("klp_clust");
	var data = {'dise': dise.value, 'klp': klp.value};
	$.ajax({
	  type: "POST",
	  url: '/content',
	  data: data,
	  //dataType: 'json',
	  success: function(response){ document.getElementById("content").innerHTML=response; },
	  error: function (xhr, ajaxOptions, thrownError) {
         	alert(xhr.status);
        	alert(thrownError);
		alert("Error");
      		}
	});
}
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
		if(trim(data[i][0])==trim(id)){
			if(flag==1)
				element.options[element.length]=new Option(data[i][2],data[i][1]);
			else{
				element.options[element.length]=new Option(data[i][1],data[i][1]);
			}
		}
	}
}

function trim(value){
//	alert(value);
	while(value[value.length-1]==' ')
		value=value.substring(0,value.length-1);
	while(value[0]==' ')
		value=value.substring(1);
//	alert(value);
	return value;
}


function replaceAll(txt, replace, with_this) {
  return txt.replace(new RegExp(replace,'g'),with_this);
}


function filter(value){
	
  	var disetable = document.getElementById("dise_table");
	var klptable = document.getElementById("klp_table");
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

function clicks(value,type){
	if(type==1){
		var table=document.getElementById('dise_table');
		for(var i=0;i<=table.rows.length-1;i++){
			table.rows[i].bgColor='#FFFFFF';
		}	
	} else {
		table=document.getElementById('klp_table');
		for(var i=0;i<=table.rows.length-1;i++){
			table.rows[i].bgColor='#FFFFFF';
		}
	}				
	if(value.bgColor=='#FFD700'){
	 	value.bgColor='#FFFFFF';
		if(type==1){
			var dise=document.getElementById('dise_value');
			dise.value='';
		
		}
		else{
			var klp=document.getElementById('klp_value');
			klp.value='';
		
		}	
	
	}
	else
	{
	 	value.bgColor='#FFD700';
		if(type==1){
			
			
			var dise=document.getElementById('dise_value');
			value_list= replaceAll(value.innerHTML,"<td>","");
			value_list= replaceAll(value_list,"</td>","|");
			value_list= value_list.substring(0,value_list.length-1);
                        //alert(value_list);
			value_list= value_list.split("|");
			dise.value=value_list.join("|");
		}
		else{
			var klp=document.getElementById('klp_value');
			value_list= replaceAll(value.innerHTML,"<td>","");
			value_list= replaceAll(value_list,"</td>","|");
			value_list= value_list.substring(0,value_list.length-1);
                        //alert(value_list);
			value_list= value_list.split("|");
			klp.value=value_list.join("|");
		}
	}
}

function formsubmit()
{
	var x;
        var y=document.getElementById("dise_value").value.split("|");
	var z=document.getElementById("klp_value").value.split("|");	
	var r=confirm("Sure to match "+y[1].trim()+" and "+z[1]+" ?");
	if (r==true)
  	{
		var data=document.URL.split("/");
		document.getElementById("matched_value").value=data[data.length-2]+"|"+data[data.length-1];
		document.forms["form1"].submit();
 	 }
	else
	{
	}
}
