var elem = "c1",
    tooltipElem = "tooltipDIV",
    charge = -300,
    colorcode = 'colored',
    colors = ['#FFC1C1', '#FFC1C2'],
    nodeSize = 'outgoing',
    directed = true,
    sortingTooltip = 'data',
    sortingOrderTooltip = true,
    tooltipSetting = 'movable',
    tooltipOrientation = 'horizontal';

function draw() {
    "use strict";

    document.getElementById('c1').innerHTML = '';

    new Networkdiagram.Chart({
        //Mandatory
        "elem": elem,
        "data": data,
        //Optional
        "tooltipElem": tooltipElem,
        "charge": charge,
        "colorcode": colorcode,
        "colors": colors,
        "nodeSize": nodeSize,
        "directed": directed,
        "sortingTooltip": sortingTooltip,
        "sortingOrderTooltip": sortingOrderTooltip,
        "tooltipSetting": tooltipSetting,
        "tooltipOrientation": tooltipOrientation,
        "onClickNode": null,
        "onClickLink": null
    });
}

function getValues() {
    "use strict";

    colorcode = document.getElementById('colorcode').options[document.getElementById('colorcode').selectedIndex].value;
    nodeSize = document.getElementById('nodeSize').options[document.getElementById('nodeSize').selectedIndex].value;
    directed = JSON.parse(document.getElementById('directed').options[document.getElementById('directed').selectedIndex].value);
    tooltipSetting = document.getElementById('tooltipSetting').options[document.getElementById('tooltipSetting').selectedIndex].value;
    sortingTooltip = document.getElementById('sortingTooltip').options[document.getElementById('sortingTooltip').selectedIndex].value;
    sortingOrderTooltip = JSON.parse(document.getElementById('sortingOrderTooltip').options[document.getElementById('sortingOrderTooltip').selectedIndex].value);
    tooltipOrientation = document.getElementById('tooltipOrientation').options[document.getElementById('tooltipOrientation').selectedIndex].value;

    draw();
}


getValues();