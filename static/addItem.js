var colorBoxArray;
var lastRGB = [-1, -1, -1];

function main()
{
    initializeHandlers();
    initializeColorSelector();
    onClick();
}

function initializeHandlers()
{
    var topBottomForm = document.getElementById("topBottomForm");
    for(var i = 0; i < 2; i++)
        topBottomForm.elements[i].onclick = onClick;

    var longShortForm = document.getElementById("longShortForm");
    for(var x = 0; x < 2; x++)
        longShortForm.elements[x].onclick = onClick;
}

function initializeColorSelector()
{
    colorBoxArray = [];
    var canvas = document.getElementById("colorSelector");
    var ctx = canvas.getContext('2d');
    var rgbArray = 
    [[255, 0, 0, 'red'], //red
    [255, 255, 0, 'yellow'], //yellow
    [255, 170, 20, 'orange'], //orange
    [150, 50, 50, 'dark purple'], //dark purple
    [100, 0, 150, 'light purple'], //light purple
    [200, 0, 255, 'brown'], //brown
    [0, 155, 0, 'green'], //green
    [190, 240, 255, 'baby blue'], //baby blue
    [0, 0, 255, 'blue'], //blue
    [0, 0, 155, 'navy blue'],
    [0, 0, 0, 'black'], //navy blue
    [254, 254, 254, 'white'],
    [200, 200, 200, 'gray']];
    var boxWidth = canvas.width / rgbArray.length;
    for(var x = 0; x < rgbArray.length && x*boxWidth < canvas.width; x++)
        colorBoxArray.push(new ColorBox(x*boxWidth, 0, boxWidth, canvas.height, rgbArray[x]));
    for(var i = 0; i < colorBoxArray.length; i++)
        colorBoxArray[i].draw(ctx);
    canvas.onclick = colorOnClick;
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
            continue;
        if(imageData.data[i] == 255 && imageData.data[i+1] == 254 && imageData.data[i+2] == 252)
            continue;
        imageData.data[i] = 254;
        imageData.data[i+1] = 254;
        imageData.data[i+2] = 254;
    }
    lastRGB[0] = 254;
    lastRGB[1] = 254;
    lastRGB[2] = 254
    ctx.putImageData(imageData, 0, 0);
}

function changeColor(r, g, b)
{
    var canvas = document.getElementById("canvas");
    var ctx = canvas.getContext('2d');
    var imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    for(var i = 0; i < imageData.data.length; i += 4)
    {
        if(imageData.data[i] == 255 && imageData.data[i+1] == 254 && imageData.data[i+2] == 252)
            continue;
        if(imageData.data[i] == lastRGB[0] && imageData.data[i+1] == lastRGB[1] && imageData.data[i+2] == lastRGB[2])
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

function colorOnClick(mouse)
{
    var x = mouse.layerX;
    var y = mouse.layerY;
    for(var i = 0; i < colorBoxArray.length; i++)
        colorBoxArray[i].onClick(x, y);
}

// Color Boc
function ColorBox(x, y, width, height, rgb)
{
    this.x = x;
    this.y = y;
    this.width = width;
    this.height = height;
    this.r = rgb[0];
    this.g = rgb[1];
    this.b = rgb[2];
    this.colorName = rgb[3];
}

ColorBox.prototype.onClick = function(x, y)
{
    if(x > this.x && x < this.x + this.width
        && y > this.y && y < this.y + this.height)
        changeColor(this.r, this.g, this.b);
};

ColorBox.prototype.draw = function(ctx)
{
    ctx.fillStyle = "rgb(" + this.r.toString() + "," + 
        this.g.toString() + "," + this.b.toString() + ")";
    ctx.fillRect(this.x, this.y, this.width, this.height);
};
// End Color Selector

function onClick()
{
    var canvas = document.getElementById("canvas");
    var ctx = canvas.getContext('2d');

    var imageId = "";
    imageId += topBottomString();
    imageId += longShortString();
    var image = document.getElementById(imageId);

    ctx.fillStyle = "rgb(255,254,252)";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(image, 0, 10, 190, 260);
    removeWaterMark();
}

function topBottomString()
{
    var clothingTypeForm = document.getElementById("topBottomForm");
    for(var i = 0; i < 2; i++)
    {
        if(clothingTypeForm.elements[i].checked)
            return clothingTypeForm.elements[i].value;
    }
    return "ERROR";
}

function longShortString()
{
    var topBottomForm = document.getElementById("longShortForm");
    for(var i = 0; i < 2; i++)
    {
        if(topBottomForm.elements[i].checked)
            return topBottomForm.elements[i].value;
    }
    return "ERROR";
}