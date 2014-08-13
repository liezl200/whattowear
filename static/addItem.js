var colorBoxArray;
var lastRGB = [-1, -1, -1];
var lastBorderColor = 0;
var colorWheel;

function main()
{
    initializeHandlers();
    initializeColorSelector();
    onClick();
}

function initializeHandlers()
{
    var mainform = document.getElementById("createItem");
    for(var i = 0; i < mainform.elements.length; i++)
    {
        var name = mainform.elements[i].name;
        if(name === "topbottom" || name === "longshort")
            mainform.elements[i].onclick = onClick;
        else if(name === "Add Item")
            mainform.elements[i].onclick = onSubmit;
    }
}

function initializeColorSelector()
{
    var canvas = document.getElementById("colorSelector");
    colorWheel = Raphael.colorwheel(canvas, 200);
    colorWheel.onchange(colorOnChange);
}

function removeWaterMark()
{
    var canvas = document.getElementById("canvas");
    var ctx = canvas.getContext('2d');
    var imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    for(var i = 0; i < imageData.data.length; i += 4)
    {
        if(imageData.data[i+3] < 1)
            continue;
        if(imageData.data[i] < 210 && imageData.data[i+1] < 210 && imageData.data[i+2] < 210)
        {
            imageData.data[i] = 0;
            imageData.data[i+1] = 0;
            imageData.data[i+2] = 0;
        }
        else
        {
            imageData.data[i] = 254;
            imageData.data[i+1] = 254;
            imageData.data[i+2] = 254;
        }
        //if(imageData.data[i] == 255 && imageData.data[i+1] == 254 && imageData.data[i+2] == 252)
        //    continue;
        
    }
    lastRGB[0] = 254;
    lastRGB[1] = 254;
    lastRGB[2] = 254;
    ctx.putImageData(imageData, 0, 0);
}

function changeColor(r, g, b)
{
    var canvas = document.getElementById("canvas");
    var ctx = canvas.getContext('2d');
    var imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    var changeBorder = false;
    var light = false
    if(r + g + b < 200 && lastBorderColor == 0)
    {
        changeBorder = true;
        light = true;
    }
    else if(r + g + b >= 200 && lastBorderColor == 255)
        changeBorder = true;
    for(var i = 0; i < imageData.data.length; i += 4)
    {
        if(imageData.data[i+3] < 1)
            continue;
        if(changeBorder)
        {
            var newBorderColor = 0;
            if(light)
                newBorderColor = 255;
            if(imageData.data[i] == lastBorderColor && imageData.data[i+1] == lastBorderColor 
                && imageData.data[i+2] == lastBorderColor)
            {
                imageData.data[i] = newBorderColor;
                imageData.data[i+1] = newBorderColor;
                imageData.data[i+2] = newBorderColor;
                lastBorderColor = newBorderColor;
            }
        }
        if(imageData.data[i] != lastBorderColor && imageData.data[i+1] != lastBorderColor 
            && imageData.data[i+2] != lastBorderColor)
        {
            imageData.data[i] = r;
            imageData.data[i+1] = g;
            imageData.data[i+2] = b;
        }
    }
    lastRGB[0] = r;
    lastRGB[1] = g;
    lastRGB[2] = b;
    ctx.putImageData(imageData, 0, 0);
}

function colorOnChange(raphaelRGB)
{
    var r = raphaelRGB.r;
    var g = raphaelRGB.g;
    var b = raphaelRGB.b;
    changeColor(r, g, b)
}

function onClick()
{
    var canvas = document.getElementById("canvas");
    var ctx = canvas.getContext('2d');

    var imageId = "";
    imageId += longShortString();
    imageId += topBottomString();
    var image = document.getElementById(imageId);

    ctx.fillStyle = "rgba(255,255,255,0)";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(image, 0, 10, 190, 260);
    removeWaterMark();
}

function onSubmit()
{
    var hiddenColor = document.getElementById('hiddenColor');
    hiddenColor.value = toHex(lastRGB[0], lastRGB[1], lastRGB[2]);
}

function topBottomString()
{
    var form = document.getElementById("createItem");
    for(var i = 0; i < form.length; i++)
    {
        if(form.elements[i].name === "longshort")
        {
            if(form.elements[i].checked)
                return form.elements[i].value;
        }
    }
    return "ERROR";
}

function longShortString()
{
    var form = document.getElementById("createItem");
    for(var i = 0; i < form.length; i++)
    {
        if(form.elements[i].name === "topbottom")
        {
            if(form.elements[i].checked)
                return form.elements[i].value;
        }
    }
    return "ERROR";
}

function toHex(r, g, b)
{
    return r.toString(16) + g.toString(16) + b.toString(16);
}