function renderShirtsMain()
{
    var container = document.getElementById('deleteItems');
    var submitButton = container.elements[0];
    var canvases = document.getElementsByTagName("canvas");
    for(var i = 0; i < canvases.length; i++) 
    {
        var canvas = canvases[i];
        var id = canvas.id;
        var parameterArray = ['','','',''];
        var count = 0;
        for(var j = 0; j < id.length; j++)
        {
            if(id.charAt(j) === ":")
                count++;
            else
                parameterArray[count] += id.charAt(j);
        }
        var rgb = getRGB(parameterArray[0]);
        var topOrBottom = parameterArray[1];
        var longOrShort = parameterArray[2];
        var pattern = parameterArray[3];
        removeWaterMark(canvas, topOrBottom, longOrShort, pattern);
        drawShirt(canvas, rgb[0], rgb[1], rgb[2]);   
    }
    submitButton.onclick = onSubmit;
}

function getRGB(hex)
{
    var r = hex.substr(0, 2);
    var g = hex.substr(2, 2);
    var b = hex.substr(4, 2);
    var rgbArray = [parseInt(r, 16), parseInt(g, 16), parseInt(b, 16)];
    return rgbArray;
}

function drawShirt(canvas, r, g, b)
{
    var ctx = canvas.getContext('2d');
    var imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    var borderColor = ((r+g+b)/3 > 100?0:255);
    for(var i = 0; i < imageData.data.length; i += 4)
    {
        if(imageData.data[i] == 255 && imageData.data[i+1] == 254 && imageData.data[i+2] == 252)
            continue;
        if(imageData.data[i] == 0 && imageData.data[i+1] == 0
            && imageData.data[i+2] == 0)
        {
            imageData.data[i] = borderColor;
            imageData.data[i+1] = borderColor;
            imageData.data[i+2] = borderColor;
        }
        else
        {
            imageData.data[i] = r;
            imageData.data[i+1] = g;
            imageData.data[i+2] = b;
        }
    }
    ctx.putImageData(imageData, 0, 0);
}

function removeWaterMark(canvas, topOrBottom, longOrShort, pattern)
{
    var ctx = canvas.getContext('2d');
    var imageId = "";
    imageId += topOrBottom;
    imageId += longOrShort;
    var image = document.getElementById(imageId);
    ctx.drawImage(image, 0, 10, canvas.width*0.9, canvas.height*0.9);
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
    ctx.putImageData(imageData, 0, 0);
}

function onSubmit()
{
    /*var container = document.getElementById("deleteItems");
    for(var i = 2; i < container.children.length; i += 6)
    {
        if(container.children[i].tagName === "BR")
            i += 1;
        var checkBox = container.elements[i+5];
        if(checkBox.checked)
    }*/
}