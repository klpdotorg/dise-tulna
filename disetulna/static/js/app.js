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
$('tr').click(function() {
	// $(this).addClass('warning').siblings().removeClass('warning');
	console.log('meh');
});

function register (type) {

}