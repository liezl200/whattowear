function renderShirtsMain()
{
	var container = document.getElementById("formContainer");
	for(var i = 0; i < container.children.length; i += 2)
	{
		if(container.children[i].tagName === "BR")
			i += 1;
		var canvas = container.children[i];
		var form = container.children[i+1];
		var rgb = getRGB(form);
		var topOrBottom = getTopOrBottom(form);
		var longOrShort = getLongOrShort(form);
		var pattern = getPattern(form);
        removeWaterMark(canvas, topOrBottom, longOrShort, pattern)
		drawShirt(canvas, rgb[0], rgb[1], rgb[2]);
	}
}

function getRGB(form)
{
	var hex = form.elements["hexValue"];
	var r = hex.value.substr(0, 2);
	var g = hex.value.substr(2, 2);
	var b = hex.value.substr(4, 2);
	var rgbArray = [parseInt(r, 16), parseInt(g, 16), parseInt(b, 16)];
	return rgbArray;
}

function getTopOrBottom(form)
{
	var topOrBottom = form.elements["topBottom"].value;
	return topOrBottom;
}

function getLongOrShort(form)
{
	var longOrShort = form.elements["longShort"].value;
	return longOrShort;
}

function getPattern(form)
{
	var pattern = form.elements["pattern"].value;
	return pattern;
}

function drawShirt(canvas, r, g, b)
{
	var ctx = canvas.getContext('2d');
	var imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    var borderColor = Math.floor((255 - (r+g+b)/3)/2);
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