function desactivarLupa() {
  if (lupaActiva) {
    var lupa = document.querySelector(".img-magnifier-glass");
    if (lupa) {
      lupa.parentNode.removeChild(lupa);
    }
    lupaActiva = false;
  }
}

function magnify(imgID) {
  var zoom = 1.75;
  var img, glass, w, h, bw;
  img = document.getElementById(imgID);
  
  /* Crear la lupa: */
  if (!lupaActiva) {
    lupaActiva = true;
  glass = document.createElement("DIV");
  glass.setAttribute("class", "img-magnifier-glass");

  /* Insertar la lupa en la imagen: */
  img.parentElement.insertBefore(glass, img);

  /* Hacer que la lupa funcione con la imagen puesta y no con otros elementos de la web: */
  glass.style.backgroundImage = "url('" + img.src + "')";
  glass.style.backgroundRepeat = "no-repeat";
  glass.style.backgroundSize = (img.width * zoom) + "px " + (img.height * zoom) + "px";
  bw = 3;
  w = glass.offsetWidth / 2;
  h = glass.offsetHeight / 2;
    
  
  /* Ejecutar la función al mover el ratón por la imagen: */
  glass.addEventListener("mousemove", moveMagnifier);
  img.addEventListener("mousemove", moveMagnifier);

  /*Aplicar la función para pantallas táctiles en la zona de la pantalla pinchada:*/
  glass.addEventListener("touchmove", moveMagnifier);
  img.addEventListener("touchmove", moveMagnifier);
  }
  function moveMagnifier(e) {
    var pos, x, y;
    /* Prevenir otras acciones que le pudan ocurrir a la imagen */
    e.preventDefault();
    /* Obtener la posición del ratón: */
    pos = getCursorPos(e);
    x = pos.x;
    y = pos.y;
    /* Evitar que el zoom se aplique fuera de la ventana de la imagen: */
    if (x > img.width - (w / zoom)) {x = img.width - (w / zoom);}
    if (x < w / zoom) {x = w / zoom;}
    if (y > img.height - (h / zoom)) {y = img.height - (h / zoom);}
    if (y < h / zoom) {y = h / zoom;}
    /* Establecer la posición de la lupa en base a la posición del ratón: */
    glass.style.left = (x - w) + "px";
    glass.style.top = (y - h) + "px";
    /* Mostrar el efecto con zoom de la lupa "sees": */
    glass.style.backgroundPosition = "-" + ((x * zoom) - w + bw) + "px -" + ((y * zoom) - h + bw) + "px";
  }

  function getCursorPos(e) {
    var a, x = 0, y = 0;
    e = e || window.event;
    /* Obtener las coordenasa de imagen: */
    a = img.getBoundingClientRect();
    /* Calcular la posición del ratón en relación a la imagen: */
    x = e.pageX - a.left;
    y = e.pageY - a.top;
    /* Mantener la posición de la lupa al sacar la posición de la imagen y  aplicar scroll a la página: */
    x = x - window.pageXOffset;
    y = y - window.pageYOffset;
    return {x : x, y : y};
  }
}