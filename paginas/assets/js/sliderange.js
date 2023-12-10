// Variable que referencia al slider
var slider = document.getElementById("rangeSlider");

// Variables que van a cambiar con el slider -> Divs
var divDescrp = document.getElementById("columnaDescr");
var divSuministro = document.getElementById("columnaSum");
var divRest = document.getElementById("columnaRest");
var divGalery = document.getElementById("galeryContainer");

// Variables que van a cambiar con el slider -> Imágenes
var img = document.getElementById("imagenCoche");
var imglogo = document.getElementById("imagenLogo");
var imagenRestringida = document.getElementById("imagenRestringida");
var imgGalery1 = document.getElementById("galeryImg1");
var imgModalGalery1 = document.getElementById("galeryModal1");
var imgGalery2 = document.getElementById("galeryImg2");
var imgModalGalery2 = document.getElementById("galeryModal2");
var imgGalery3 = document.getElementById("galeryImg3");
var imgModalGalery3 = document.getElementById("galeryModal3");

// Variables que van a cambiar con el slider -> Texto
var tituloSponsor = document.getElementById("nombreSponsor");
var descripcionSponsor = document.getElementById("descripcionSponsor");
var sponsorOficial = document.getElementById("sponsorOficial");
var infoSponsor = document.getElementById("infoSponsor");
var restriccionSponsor = document.getElementById("restriccionSponsor");
var descripSponsor = document.getElementById("descripSponsor");

// Variables para recoger todos los divs del equipo seleccionado, tipo: HTMLColection <HTMLDivElement>>
var divSponsor = document.getElementById("infoOculta").getElementsByTagName("div");
var filaInfo = document.getElementById("filaInfo").querySelectorAll("img, h3");

// Variable en la que se guradarán los nodos hijos de "divSponsor", tipo: NodeListOf<ChildNode>
var etiquetas;

// Variable global para el estado de la lupa
var lupaActiva = false;

// Variable en la que se localiza el valor de los nodos de "etiquetas", tipo: array bidimensional
var info = [];

var sponsorsOfi = [];
var cont = 0;

var suminsText = "";

// Array con las fotos del patrocinador para la galería
var arrayGaleria = JSON.parse(resultadoGaleria);
console.log(arrayGaleria);

// Bucle para almacenar la información en "info"
for (var i = 0; i < divSponsor.length; i++){
  etiquetas = divSponsor.item(i).childNodes;
  info[i] = [];
  
  for(var a = 0; a < etiquetas.length; a++){
    if(etiquetas.item(a).nodeName == "P"){
      info[i][a] = etiquetas.item(a).innerHTML;
      
      if (a == 1 && etiquetas.item(a).innerHTML == "si"){
        sponsorsOfi[cont] = i;
        cont++;
      }

    } else if (etiquetas.item(a).nodeName == "IMG"){
      info[i][a] = etiquetas.item(a).src;
    }
  }
}

if (sponsorsOfi.length == 1){
  document.getElementById("tituloSOficial").innerText = "Patrocinador principal";
  filaInfo[0].src = info[sponsorsOfi[0]][21];
  filaInfo[1].innerText = divSponsor.item(sponsorsOfi[0]).id;
  document.getElementById("sponsorOficial2").style.display = "none";
} else {
  document.getElementById("tituloSOficial").innerText = "Patrocinadores principales";
  filaInfo[0].src = info[sponsorsOfi[0]][21];
  filaInfo[1].innerText = divSponsor.item(sponsorsOfi[0]).id;
  filaInfo[2].src = info[sponsorsOfi[1]][21];
  filaInfo[3].innerText = divSponsor.item(sponsorsOfi[1]).id;
}

//console.log(info);

function comprobarExistenciaImagen(url, callback) {
  var imagen = new Image();
            
  imagen.onload = function() {
    callback(true); // La imagen existe
  };
            
  imagen.onerror = function() {
    callback(false); // La imagen no existe
  };
  imagen.src = url;
}

// Función para mostrar el valor del slider
function rangeSlide(value){
  document.getElementById('rangeValue').innerHTML = value;
}

// Evento actuador que efectuará los cambios en el contenido de la página
slider.addEventListener("input", function() {
  const value = parseInt(this.value, 10);

  switch(value){ 
    case 0: 
        divDescrp.style.display = "none";
        divSuministro.style.display = "none";
        divRest.style.display = "none";
        divGalery.style.display = "none";

        img.src = info[value][0];
        imglogo.src = info[value][2].slice(0, info[value][2].length - 4);
        imagenRestringida.src = "";
        
        desactivarLupa();
        magnify("imagenCoche");
                
        tituloSponsor.textContent = "";
        descripcionSponsor.textContent = "";
        infoSponsor.innerText = "";
        restriccionSponsor.textContent = "";
        document.getElementById("tituloRest").innerText = "";

      break;
    default:
      if (value >= 1 && value <= info.length) {
        divDescrp.style.display = "block";
        divSuministro.style.display = "block";
        divGalery.style.display = "block";
        
        if(info[value][3] != "no"){
          suminsText = "este patrocinador aporta " + info[value][3].toLowerCase();

        } else {
          suminsText = "este patrocinador no aporta nigún tipo suministro material";
        }

        img.src = info[value][7];
        imglogo.src = info[value][21];

        desactivarLupa();
        magnify("imagenCoche");

        tituloSponsor.textContent = divSponsor.item(value).id;
        descripcionSponsor.textContent = info[value][9];

        infoSponsor.innerText = divSponsor.item(value).id + " se fundó en el año " + info[value][17] + 
          " en " + info[value][13] + ", y el tipo patrocinio que aporta al equipo está centrado en el sector de industria " + 
          info[value][11].toLowerCase() + ". Su especialidad es " + info[value][15].toLowerCase() + ", y " + suminsText;
        
        if (value != 0){
          imgGalery1.src = arrayGaleria[(value-1)]["ruta"];
          imgModalGalery1.src = arrayGaleria[(value-1)]["ruta"];

          if(arrayGaleria[(value-1)]["ruta2"] == " "){
            document.getElementById("colGalery2").style.display = "none";
          } else {
            document.getElementById("colGalery2").style.display = "block";

            imgGalery2.src = arrayGaleria[(value-1)]["ruta2"];
            imgModalGalery2.src = arrayGaleria[(value-1)]["ruta2"];
          }
          
          if(arrayGaleria[(value-1)]["ruta3"] == " "){
            document.getElementById("colGalery3").style.display = "none";
          } else {
            document.getElementById("colGalery3").style.display = "block";
            
            imgGalery3.src = arrayGaleria[(value-1)]["ruta3"];
            imgModalGalery3.src = arrayGaleria[(value-1)]["ruta3"];
          }

        }        

        if (info[value][19] == "no"){
          divRest.style.display = "none";
          document.getElementById("tituloRest").innerText = "";
          restriccionSponsor.textContent = "";

        } else {
          divRest.style.display = "block";
          document.getElementById("tituloRest").innerText = "Restricción de patrocinio";
          
          restriccionSponsor.innerText = "La restricción que tiene este patrocinador es debido a " + info[value][19] + ". ";
          descripSponsor.innerText = info[value][23];
            
          imagenRestringida.src = info[value][25];
        }
        
      } else {
        console.log("Valor inválido");
      }
      break;
  }

});
// Variable que referencia al slider
var slider = document.getElementById("rangeSlider");

// Variables que van a cambiar con el slider -> Divs
var divDescrp = document.getElementById("columnaDescr");
var divSuministro = document.getElementById("columnaSum");
var divRest = document.getElementById("columnaRest");
var divGalery = document.getElementById("galeryContainer");

// Variables que van a cambiar con el slider -> Imágenes
var img = document.getElementById("imagenCoche");
var imglogo = document.getElementById("imagenLogo");
var imagenRestringida = document.getElementById("imagenRestringida");
var imgGalery1 = document.getElementById("galeryImg1");
var imgModalGalery1 = document.getElementById("galeryModal1");
var imgGalery2 = document.getElementById("galeryImg2");
var imgModalGalery2 = document.getElementById("galeryModal2");
var imgGalery3 = document.getElementById("galeryImg3");
var imgModalGalery3 = document.getElementById("galeryModal3");

// Variables que van a cambiar con el slider -> Texto
var tituloSponsor = document.getElementById("nombreSponsor");
var descripcionSponsor = document.getElementById("descripcionSponsor");
var sponsorOficial = document.getElementById("sponsorOficial");
var infoSponsor = document.getElementById("infoSponsor");
var restriccionSponsor = document.getElementById("restriccionSponsor");
var descripSponsor = document.getElementById("descripSponsor");

// Variables para recoger todos los divs del equipo seleccionado, tipo: HTMLColection <HTMLDivElement>>
var divSponsor = document.getElementById("infoOculta").getElementsByTagName("div");
var filaInfo = document.getElementById("filaInfo").querySelectorAll("img, h3");

// Variable en la que se guradarán los nodos hijos de "divSponsor", tipo: NodeListOf<ChildNode>
var etiquetas;

// Variable global para el estado de la lupa
var lupaActiva = false;

// Variable en la que se localiza el valor de los nodos de "etiquetas", tipo: array bidimensional
var info = [];

var sponsorsOfi = [];
var cont = 0;

var suminsText = "";

// Array con las fotos del patrocinador para la galería
var arrayGaleria = JSON.parse(resultadoGaleria);
console.log(arrayGaleria);

// Bucle para almacenar la información en "info"
for (var i = 0; i < divSponsor.length; i++){
  etiquetas = divSponsor.item(i).childNodes;
  info[i] = [];
  
  for(var a = 0; a < etiquetas.length; a++){
    if(etiquetas.item(a).nodeName == "P"){
      info[i][a] = etiquetas.item(a).innerHTML;
      
      if (a == 1 && etiquetas.item(a).innerHTML == "si"){
        sponsorsOfi[cont] = i;
        cont++;
      }

    } else if (etiquetas.item(a).nodeName == "IMG"){
      info[i][a] = etiquetas.item(a).src;
    }
  }
}

if (sponsorsOfi.length == 1){
  document.getElementById("tituloSOficial").innerText = "Patrocinador principal";
  filaInfo[0].src = info[sponsorsOfi[0]][21];
  filaInfo[1].innerText = divSponsor.item(sponsorsOfi[0]).id;
  document.getElementById("sponsorOficial2").style.display = "none";
} else {
  document.getElementById("tituloSOficial").innerText = "Patrocinadores principales";
  filaInfo[0].src = info[sponsorsOfi[0]][21];
  filaInfo[1].innerText = divSponsor.item(sponsorsOfi[0]).id;
  filaInfo[2].src = info[sponsorsOfi[1]][21];
  filaInfo[3].innerText = divSponsor.item(sponsorsOfi[1]).id;
}

//console.log(info);

function comprobarExistenciaImagen(url, callback) {
  var imagen = new Image();
            
  imagen.onload = function() {
    callback(true); // La imagen existe
  };
            
  imagen.onerror = function() {
    callback(false); // La imagen no existe
  };
  imagen.src = url;
}

// Función para mostrar el valor del slider
function rangeSlide(value){
  document.getElementById('rangeValue').innerHTML = value;
}

// Evento actuador que efectuará los cambios en el contenido de la página
slider.addEventListener("input", function() {
  const value = parseInt(this.value, 10);

  switch(value){ 
    case 0: 
        divDescrp.style.display = "none";
        divSuministro.style.display = "none";
        divRest.style.display = "none";
        divGalery.style.display = "none";

        img.src = info[value][0];
        imglogo.src = info[value][2].slice(0, info[value][2].length - 4);
        imagenRestringida.src = "";
        
        desactivarLupa();
        magnify("imagenCoche");
                
        tituloSponsor.textContent = "";
        descripcionSponsor.textContent = "";
        infoSponsor.innerText = "";
        restriccionSponsor.textContent = "";
        document.getElementById("tituloRest").innerText = "";

      break;
    default:
      if (value >= 1 && value <= info.length) {
        divDescrp.style.display = "block";
        divSuministro.style.display = "block";
        divGalery.style.display = "block";
        
        if(info[value][3] != "no"){
          suminsText = "este patrocinador aporta " + info[value][3].toLowerCase();

        } else {
          suminsText = "este patrocinador no aporta nigún tipo suministro material";
        }

        img.src = info[value][7];
        imglogo.src = info[value][21];

        desactivarLupa();
        magnify("imagenCoche");

        tituloSponsor.textContent = divSponsor.item(value).id;
        descripcionSponsor.textContent = info[value][9];

        infoSponsor.innerText = divSponsor.item(value).id + " se fundó en el año " + info[value][17] + 
          " en " + info[value][13] + ", y el tipo patrocinio que aporta al equipo está centrado en el sector de industria " + 
          info[value][11].toLowerCase() + ". Su especialidad es " + info[value][15].toLowerCase() + ", y " + suminsText;
        
        if (value != 0){
          imgGalery1.src = arrayGaleria[(value-1)]["ruta"];
          imgModalGalery1.src = arrayGaleria[(value-1)]["ruta"];

          if(arrayGaleria[(value-1)]["ruta2"] == " "){
            document.getElementById("colGalery2").style.display = "none";
          } else {
            document.getElementById("colGalery2").style.display = "block";

            imgGalery2.src = arrayGaleria[(value-1)]["ruta2"];
            imgModalGalery2.src = arrayGaleria[(value-1)]["ruta2"];
          }
          
          if(arrayGaleria[(value-1)]["ruta3"] == " "){
            document.getElementById("colGalery3").style.display = "none";
          } else {
            document.getElementById("colGalery3").style.display = "block";
            
            imgGalery3.src = arrayGaleria[(value-1)]["ruta3"];
            imgModalGalery3.src = arrayGaleria[(value-1)]["ruta3"];
          }

        }        

        if (info[value][19] == "no"){
          divRest.style.display = "none";
          document.getElementById("tituloRest").innerText = "";
          restriccionSponsor.textContent = "";

        } else {
          divRest.style.display = "block";
          document.getElementById("tituloRest").innerText = "Restricción de patrocinio";
          
          restriccionSponsor.innerText = "La restricción que tiene este patrocinador es debido a " + info[value][19] + ". ";
          descripSponsor.innerText = info[value][23];
            
          imagenRestringida.src = info[value][25];
        }
        
      } else {
        console.log("Valor inválido");
      }
      break;
  }

});
