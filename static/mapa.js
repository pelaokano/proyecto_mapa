var url_string = window.location.href;
var url = new URL(url_string);
var urlLon = url.searchParams.get("lon");
var urlLat = url.searchParams.get("lat");

function isNumeric(n) {
  return !isNaN(parseFloat(n)) && isFinite(n);
}

//console.log(urlLon,urlLat)

//se crea el objeto map a partir de la libreria leaflet
var map = L.map('map');

map.doubleClickZoom.disable();

//se agregan las capas con las imagenes de los mapas, se podria buscar alguna imagen mejor
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a>"
}).addTo(map);

if (urlLon != null && urlLat != null){
	map.setView([parseFloat(urlLat), parseFloat(urlLon)], 9)
	let latlng1 = new L.latLng(urlLat, urlLon);
	L.marker(latlng1).addTo(map);
}else{
	map.setView([-33.4569400, -70.6482700], 9)
}

var seIcon = L.icon({
    iconUrl: my_icono,
    iconSize: [30, 35],
    iconAnchor: [10, 25],
    popupAnchor: [0, -28]
});

//funcion para extraer un parametro de las cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            };
        };
    };
    return cookieValue;
;}

//se extrae el codigo csrf que usa django para seguridad
let csrftoken1 = getCookie('csrftoken');
//console.log(csrftoken1)

//funcion para enviar solicitud post a un servidor django con codigo csrf
async function postData(url = '', csrftoken, dataPost, data = {}) {
  const response = await fetch(url, {
    method: 'POST',
    mode: 'same-origin',
    
    headers: {'X-CSRFToken': csrftoken},

    body: dataPost
  });
  return response.json();
};

//variables globales para definir objetos que continen a capas de lineas y subestaciones
capasSE = new Object();
capasLinea = new Object();

function popupSE(feature, layer) {
    if (feature.properties && feature.properties.nombre && feature.properties.id) {
        layer.bindPopup(
		"<strong>Nombre: </strong>" + feature.properties.nombre + 
		"<br>" + 
		"<strong>ID: </strong>" + feature.properties.id +
		"</br>" +
		"<strong>Region: </strong>" + feature.properties.region +
		"</br>" +
		"<strong>Coordenadas: </strong>" + feature.geometry.coordinates +
		"</br>" +
		"<a href='" + feature.properties.url_se + "' target='_blank'>Infotecnica</a> ");
    }}

function popupLinea(feature, layer) {
    if (feature.properties && feature.properties.nombre) {
        layer.bindPopup(
		"<strong>Nombre: </strong>" + feature.properties.nombre + 
		"<br>" + 
		"<strong>Tension: </strong>" + feature.properties.tension +
		"</br>" +
		"<strong>Largo: </strong>" + feature.properties.Largo);
    }}

//funcion para crear capa de las subestaciones
function crearCapaGeoJsonPunto(data){
	let capaGeoJson = L.geoJson(data, {
		pointToLayer: function (feature, latlng) {
			return L.marker(latlng,{ icon: seIcon });
		}, onEachFeature: popupSE
	});
	return capaGeoJson;
}

//colores hex para lineas
coloresLinea = {
'220':'#00FF00', //verde
'154':'#FF0000', //rojo
'500':'#0000FF', //azul
'66':'#FF00FF', //fucsia
'110':'#FF8000', //naranja
'345':'#000000', //negro
'44':'#FFFF00' //amarillo
}

function cambiarEstiloCapa(capaGejson) {

    capaGejson.eachLayer(function(elemento) {
        let tension = elemento.feature.properties['tension'];
	
        elemento.setStyle({
            'color': coloresLinea[tension],
			'weight': 3,
            'opacity': 1
        });
    });
}

//funcion para crear capas de las lineas
function crearCapaGeoJsonLinea(data,color){
	
	let estiloLinea = {
    "color": coloresLinea[color],
    "weight": 3,
    "opacity": 1
	};
	
	let capaGeoJson = L.geoJson(data, {
		
		style: estiloLinea, onEachFeature: popupLinea
	});
	return capaGeoJson;	
}

//codigo para a partir de una lista de checkbox poder solicitar información al servidor de las lineas filtrando por tensión
document.querySelectorAll("input[id^='cbox_tension']").forEach(item => {
  item.addEventListener('click', event => {
    if (event.target.checked==true) {
		let formData = new FormData();
		formData.append('tension', event.target.value);
		//postData('http://127.0.0.1:8000/api/v1/enviar_geojsonLinea2', csrftoken1, formData, { answer: 42 })
		postData('/api/v1/enviar_geojsonLinea2', csrftoken1, formData, { answer: 42 })
		.then((data) => {
			//aqui se debiera colocar el codigo para dibujar los puntos
			console.log(data);
			capasLinea[event.target.value]=crearCapaGeoJsonLinea(data,event.target.value);
			map.addLayer(capasLinea[event.target.value]);
			console.log(capasLinea);
			console.log(event.target.value)
		});
	} else if(event.target.checked==false){
		map.removeLayer(capasLinea[event.target.value]);
		delete capasLinea[event.target.value];
		console.log(capasLinea);
		
	}
  });
});

//codigo para a partir de una lista de checkbox poder solicitar información al servidor de las subestaciones filtrando por region
document.querySelectorAll("input[id^='cbox_se_']").forEach(item => {
  item.addEventListener('click', event => {
    if (event.target.checked==true) {
		let formData = new FormData();
		formData.append('region', event.target.value);
		//postData('http://127.0.0.1:8000/api/v1/geojson_puntosSE2', csrftoken1, formData, { answer: 42 })
		postData('/api/v1/geojson_puntosSE2', csrftoken1, formData, { answer: 42 })
		.then((data) => {
			//aqui se debiera colocar el codigo para dibujar los puntos
			capasSE[event.target.value]=crearCapaGeoJsonPunto(data);
			//let capa = crearCapaGeoJson(data);
			//map.addLayer(capa);
			map.addLayer(capasSE[event.target.value]);
			console.log(capasSE);
		});
	} else if (event.target.checked==false){
		map.removeLayer(capasSE[event.target.value]);
		delete capasSE[event.target.value];
		console.log(capasSE);
	}
  });
});

//agregar un marcador al hacer doble click
validador = true;

inlat = 0;
inlon = 0;

capasSE_filtro = new Object();
capasLinea_filtro = new Object();
marcador = new Object();

function contenidoPopup(latitud,longitud){

contenido = '<table><th colspan="2"style="text-align: center">Buscar Instalaciones</th>' +
			'<tr><td><label for="name1">Latitud: </label></td>' +
			'<td><input type="text" id="name1" size="10" value="' + latitud + '" disabled></td></tr>'+
			'<tr><td><label for="name2">Longitud: </label></td>' +
			'<td><input type="text" id="name2" size="10" value="' + longitud + '" disabled></td></tr>' +
			'<tr><td><label for="distancia">Distancia: </label></td>' +
			'<td><input type="text" id="distancia" size="10"></td></tr>' +
			//'<script>distancia = document.getElementById("distancia").value;</script>' +
			
			'<tr><td colspan="2" style="text-align: center">' +
			'<input id="buscar" type="button" value="Buscar" onclick="buscarInstalaciones();"/>' +
			'</td></tr></table>';
			
return contenido;

}

function crearMarcador(Lat_Lon){
	
    if (validador) {
        marcador = L.marker(Lat_Lon).addTo(map);
		marcador.bindPopup(contenidoPopup(Lat_Lon.lat,Lat_Lon.lng)).openPopup();
        validador = false
		inlat = Lat_Lon.lat;
		inlon = Lat_Lon.lng;
    } else {
        map.removeLayer(marcador);
		map.removeLayer(capasSE_filtro);
		map.removeLayer(capasLinea_filtro);
        marcador = L.marker(Lat_Lon).addTo(map);
		marcador.bindPopup(contenidoPopup(Lat_Lon.lat,Lat_Lon.lng)).openPopup();
		inlat = Lat_Lon.lat;
		inlon = Lat_Lon.lng;
    }
}

map.on('dblclick', function (e) {
	crearMarcador(e.latlng);
});

function buscarInstalaciones(){
	
	distancia = document.getElementById("distancia").value;
	//console.log(distancia)
	
	if (isNumeric(distancia)){
		if (parseFloat(distancia) <= 0){
			alert('La distancia debe ser mayor que 0')
		}else{
			
			let formData = new FormData();
			formData.append('latitud', inlat);
			formData.append('longitud', inlon);
			formData.append('distancia', parseFloat(distancia));

			postData('/api/v1/enviar_geojsonFiltroPunto', csrftoken1, formData, { answer: 42 })
			.then((data) => {
				
				capasSE_filtro = crearCapaGeoJsonPunto(data['SSEE']);
				capasLinea_filtro = crearCapaGeoJsonLinea(data['Lineas'],'220');
				cambiarEstiloCapa(capasLinea_filtro);
				map.addLayer(capasSE_filtro);
				map.addLayer(capasLinea_filtro);
			});
		}
	}else{
		alert('La distancia debe ser un numero')
	}	
}

function limpiarMapa(){
	map.removeLayer(marcador);
	map.removeLayer(capasSE_filtro);
	map.removeLayer(capasLinea_filtro);
	document.getElementById("inp_latitud").value = ''
	document.getElementById("inp_longitud").value = ''
}

function AgregarMarcador(){
	
	let latitud = parseFloat(document.getElementById("inp_latitud").value);
	let longitud = parseFloat(document.getElementById("inp_longitud").value);
	
	if (isNumeric(latitud) && isNumeric(longitud)){
		let latlng = L.latLng(latitud, longitud);
		crearMarcador(latlng);
		document.getElementById("inp_latitud").value = ''
		document.getElementById("inp_longitud").value = ''
	}else{
		alert('La latitud y longitud deben ser numeros');
	}		
}




