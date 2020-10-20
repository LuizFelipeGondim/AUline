
//Mapa feito por Ruan Pablo +_-
	
//Pega cordenadas, adiciona na Lista Ordenada e transforma em Link
var pegarValores = function(){

    var lat = resposta.features[0].center[1];
	var long = resposta.features[0].center[0];
	
	var mapa = document.createElement('div');
	mapa.setAttribute("id","mapa");
	document.getElementById('map').appendChild(mapa);

	mapa.style.height="400px";
		
	CriarMap(lat,long);

	}

//Onde o mapa é gerado
function CriarMap(lat1,long1){
	var mymap = L.map('mapa').setView([lat1,long1], 16);

	L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibHVpemZnYSIsImEiOiJja2dneXF0YTcxbXp1MnJwNGNkNXJldHZ0In0.WkHL-ShT9LVbrKYdVitQDw', {
		attribution: '© <a href="https://www.mapbox.com/about/maps/">Mapbox</a> © <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> <strong><a href="https://www.mapbox.com/map-feedback/" target="_blank">Improve this map</a></strong>',
		tileSize: 512,
		maxZoom: 18,
		zoomOffset: -1,
		id: 'mapbox/streets-v11',
		accessToken: 'pk.eyJ1IjoibHVpemZnYSIsImEiOiJja2dneXF0YTcxbXp1MnJwNGNkNXJldHZ0In0.WkHL-ShT9LVbrKYdVitQDw'
	}).addTo(mymap);
	
	L.marker([lat1,long1]).addTo(mymap)
		.bindPopup("<b>Atenção!</b><br />Local onde o animal pode ser encontrado").openPopup();
	L.circle([lat1,long1], 400, {
		color: 'red',
		fillColor: '#f03',
		fillOpacity: 0.5
	}).addTo(mymap)
}

//Funções em conjunto para fazer a requisição na API;
function reqListener() {
	var request = this.responseText; 
	return request;	
}

var resposta;
function GerarCoordenadas(endereco){
    oReq = new XMLHttpRequest();
    oReq.onload = reqListener;
    oReq.open("get","https://api.mapbox.com/geocoding/v5/mapbox.places/"+endereco+".json?access_token=sk.eyJ1Ijoib3J1YW4iLCJhIjoiY2sxYmEwbW53MDJpeDNvcGN4Mm5mYWYwciJ9.wuSyAqEfN8SFraG1v9jE8Q");
	oReq.onreadystatechange = function(e) {
        if(this.readyState == 4){
			resposta = JSON.parse(this.responseText);
			pegarValores();
		}
	}
	oReq.send();
}

//Funcao principal, chama todas outras em uma sequência lógica;
function main(){
    const endereco = JSON.parse(document.getElementById('endereco').textContent);
	GerarCoordenadas(endereco);
}