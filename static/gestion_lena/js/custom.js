var url_api = "http://localhost:8000/api/v1/";
var url = "http://fcoramirezz.pythonanywhere.com/api/v1/";
var URL_API_PRODUCCTION = url;

function regionCambio(value){
    if (isNaN(parseInt(value))){ // No es Numero
        $('#selector_provincia').empty();
        $('#selector_comuna').empty();
    }else{
        var provinciaSelector = $('#selector_provincia');

        provinciaSelector.empty(); // borrar opciones provincias

        //configurar provincias
        $.getJSON( URL_API_PRODUCCTION+"provincia/?format=json&region="+value, function (data) {
            $.each(data.objects , function( key, val ) {
                var option = "<option></option>";
                if (key == 0){ // primer elemento
                    provinciaCambio(val.id);
                    option = "<option selected='selected'></option>";
                }
                provinciaSelector.append($(option).attr("value", val.id).text(val.nombre));
            });
        });
    }
}

function provinciaCambio(value){
    var comunaSelector = $('#selector_comuna');
    comunaSelector.empty(); // borrar opciones provincias
    $.getJSON( URL_API_PRODUCCTION+"comuna/?format=json&provincia="+value, function (data) {
        $.each(data.objects , function( key, val ) {
            var option = "<option></option>";
            if (key == 0){
                option = "<option selected='selected'></option>";
            }
            comunaSelector.append($(option).attr("value", val.id).text(val.nombre));
        });
    });
}


/* Actualizacion */

function direccionActualizacion(){
            id_region = $('#selector_region').val();
            id_provincia = $('#selector_provincia').val();
            id_comuna = $('#selector_comuna').val();
            //regionCambio(id_region);
            $('#selector_region').val(id_region);
            $('#selector_provincia').empty();
            $.getJSON(URL_API_PRODUCCTION+"provincia/?format=json&region="+id_region, function (data) {
                $.each(data.objects , function( key, val ) {
                    $('#selector_provincia').append($("<option></option>").attr("value", val.id).text(val.nombre));
                });
            }).done(function(){
                $('#selector_provincia').val(id_provincia);
                $('#selector_comuna').empty();
                $.getJSON(URL_API_PRODUCCTION+"comuna/?format=json&provincia="+id_provincia, function (data) {
                    $.each(data.objects , function( key, val ) {
                        $('#selector_comuna').append($("<option></option>").attr("value", val.id).text(val.nombre));
                    });
                }).done(function(){
                    $('#selector_comuna').val(id_comuna);
                });
            }).done(function(){
                console.log("Ready");
            });
}

/* EndActualizacion */


function llenarSelectores(){
    var selected = $('#selector_region option:selected').val();
    if (!isNaN(parseInt(selected))){ // es un numero (predefinido) actualizacion
        direccionActualizacion();
    }else{ // creacion
        $('#selector_provincia').empty();
        $('#selector_comuna').empty();
    }
}

/* Contacto   */

function pedidoLlenarDireccion(value){
    if (!isNaN(parseInt(value))){ // es un numero
        var id_region;
        var id_provincia;
        var id_comuna;
        var direccion;
        $.getJSON( URL_API_PRODUCCTION+"contacto/"+ value +"/?format=json", function (data) {
            id_region = data.region.id;
            id_provincia = data.provincia.id;
            id_comuna = data.comuna.id;
            direccion = data.direccion;
            //regionCambio(id_region);
            $('#selector_region').val(id_region);
            $('#selector_provincia').empty();
            $.getJSON(URL_API_PRODUCCTION+"provincia/?format=json&region="+id_region, function (data) {
                $.each(data.objects , function( key, val ) {
                    $('#selector_provincia').append($("<option></option>").attr("value", val.id).text(val.nombre));
                });
            }).done(function(){
                $('#selector_provincia').val(id_provincia);
                $('#selector_comuna').empty();
                $.getJSON(URL_API_PRODUCCTION+"comuna/?format=json&provincia="+id_provincia, function (data) {
                    $.each(data.objects , function( key, val ) {
                        $('#selector_comuna').append($("<option></option>").attr("value", val.id).text(val.nombre));
                    });
                }).done(function(){
                    $('#selector_comuna').val(id_comuna);
                });
            });
        }).done(function() {
            $('#id_direccion_destino').val(direccion);
        });
    }else{
        $('#selector_region').val("");
        $('#selector_provincia').empty();
        $('#selector_comuna').empty();
        $('#id_direccion_destino').val("");
    }
}

/* end Contacto   */

//
$(function() {
    llenarSelectores();
    $('.checkbox').click(function(){
        var largo = document.getElementsByClassName("checkbox").length;
        var cantidad = $('input:checked').length;
        $('#cantidad_seleccionados').text(cantidad+" pedido seleccionados de " + largo);
    });
     $.datepicker.setDefaults($.datepicker.regional['es']);
        $('.dateinput').datepicker({ format: "yyyy/mm/dd",
            changeYear: true,
            changeMonth: true,
            numberOfMonths: 2,
            yearRange: "-1:+2"});
     $('#tabla_adapted').dataTable({
                "sPaginationType": "full_numbers",
                "oLanguage": {
                    "sUrl": "/static/gestion_lena/translate/spanish.txt"
                }
     });
});