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
        if(imageData.data[i] < 180 && imageData.data[i+1] < 180 && imageData.data[i+2] < 180)
        {
            imageData.data[i] = 0;
            imageData.data[i+1] = 0;
            imageData.data[i+2] = 0;
        }
        else
        {
            imageData.data[i] = 255;
            imageData.data[i+1] = 255;
            imageData.data[i+2] = 255;
        }
    }
    lastRGB[0] = 255;
    lastRGB[1] = 255;
    lastRGB[2] = 255;
    ctx.putImageData(imageData, 0, 0);
}

function changeColor(r, g, b)
{
    var canvas = document.getElementById("canvas");
    var ctx = canvas.getContext('2d');
    var imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    var newBorderColor = ((r+g+b)/3 > 100?0:255);
    for(var i = 0; i < imageData.data.length; i += 4)
    {
        if(imageData.data[i+3] < 1)
            continue;
        if(imageData.data[i] == lastBorderColor && imageData.data[i+1] == lastBorderColor 
            && imageData.data[i+2] == lastBorderColor)
        {
            imageData.data[i] = newBorderColor;
            imageData.data[i+1] = newBorderColor;
            imageData.data[i+2] = newBorderColor;
        }
        else
        {
            imageData.data[i] = r;
            imageData.data[i+1] = g;
            imageData.data[i+2] = b;
        }
    }
    lastBorderColor = newBorderColor;
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
    changeColor(r, g, b);
}

function onClick()
{
    var canvas = document.getElementById("canvas");
    var ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
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
    var hex = toHex(lastRGB[0], lastRGB[1], lastRGB[2]);
    hiddenColor.value = hex;
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
    r = Math.floor(r);
    g = Math.floor(g);
    b = Math.floor(b);
    var rString = r.toString(16);
    if(rString.length < 2)
        rString = "0" + rString;
    var gString = g.toString(16);
    if(gString.length < 2)
        gString = "0" + gString;
    var bString = b.toString(16);
    if(bString.length < 2)
        bString = "0" + bString;
    return  rString + gString + bString;
}