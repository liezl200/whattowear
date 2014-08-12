function renderShirtsMain()
{
	var container = document.getElementById("formContainer");
	for(var i = 0; i < container.children.length; i += 2)
	{
		var canvas = container.children[i];
		var form = container.children[i+1];
		var rgb = getRGB(form);
		var topOrBottom = getTopOrBottom(form);
		var longOrShort = getLongOrShort(form);
		var pattern = getPattern(form);
		drawShirt(canvas, rgb[0], rgb[1], rgb[2], topOrBottom, longOrShort, pattern);
	}

}

function getRGB(form)
{
	var hex = form.elements["hexValue"];
	var r = hex.value.substr(0, 2);
	var g = hex.value.substr(2, 2);
	var b = hax.value.substr(4, 2);
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

function drawShirt(canvas, r, g, b, topOrBottom, longOrShort, pattern)
{
	var ctx = canvas.getContext('2d');
	var imageId = "";
	imageId += getLongOrShort();
	imageId += getTopOrBottom();
	var image = document.getElementById(imageId);
	ctx.drawImage(image, 0, 10, 95, 130);
}