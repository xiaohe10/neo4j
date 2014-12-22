Network
=======
# Getting started
Before getting started the following libraries and documents have to be included on your website:
* D3.min.js
* jquery-1.11.1.js
* colorGenerator.js
* network.js
* network.css

# Your First Chart
First of all you add a `<div>` tag with an ID to your website. The `<div>`is the place where the graphic will be placed. The ID will be given to the network library, so it knows where to draw the chart.
You can also add a second `<div>`tag for the tooltip. The second `<div>` tag is optional but if you want to show the tooltips as static text it is required.
In the next step you add the following javascript code in your website. You can do that directly in the html page by writing the code between two `<script>` tags  or you write an own .js file 
and include this file on the website.

The code should contain the following lines of code:

```javascript
var data = [
    { source: "Augsburg", target: "Bremen", value: 5 },
    { source: "Bremen", target: "Augsburg", value: 2 },
    { source: "Bremen", target: "Hamburg", value: 8 },
    { source: "Augsburg", target: "Chemnitz", value: 6 },
    { source: "Chemnitz", target: "Bremen", value: 2 },
    { source: "Hamburg", target: "Augsburg", value: 2 },
    { source: "München", target: "Augsburg", value: 4 }
];

new Networkdiagram.Chart({
        //Mandatory
        "elem": elem,
        "data": data,
        //Optional
        "charge": charge,
        "colorcode": colorcode,                         //possible values: ['colored', 'black-white']
        "colors": colors,
        "nodeSize": nodeSize,                           //possible values: ['outgoing', 'incoming']
        "directed": directed,                           //possible values: [true, false] true means directed, false means undirected
        "sortingTooltip": sortingTooltip,               //possible values: [label, color, outgoingTotal, incominTotal, total, numberOfLinks]
        "sortingOrderTooltip": sortingOrderTooltip,     //possible values: [true, false] true means ascending, false means descending
        "tooltipSetting": tooltipSetting,
        "onClickNode": null,
        "onClickLink": null
});
```

## Mandatory Attributes
<table>
    <tr>
        <th>Attribute</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>data</td>
        <td>contains all connections which should be displayed in the network diagram. The structure of data is an array with several objects as the following:
            <br />{   source:   name of the node from which the connection comes
            <br />target:   name of the node to which the connection goes
            <br />value:    strength of the link
            <br />}
            <br /><br />possible values: any in the above described format
        </td>
    </tr>
    <tr>
        <td>elem</td>
        <td>is the id of a 'div' tag in which the network diagram should be drawn
            <br /><br />possible values: any valid id of a 'div' tag
        </td>
    </tr>
</table>

## Optional Attributes
<table>
    <tr>
        <th>Attribute</th>
        <th>Description</th>
    </tr>
    <tr>
		<td>tooltipElem</td>
		<td>is the id of a 'div' where the tooltip should appear. If the tooltip should be movable or no tooltip should be shown, the element can remain empty
			<br /><br />default: null
			<br />possible values: any valid id of a 'div' or null
		</td>
	</tr>
	<tr>
		<td>charge</td>
		<td>is a technical attribute for the settings of the network.
			<br /><br />default: -300
			<br />possible values: any number
		</td>
	</tr>
	<tr>
		<td>colorcode</td>
		<td>defines if the nodes should be drawn in black-white or with colors
			<br /><br />default: 'colored'
			<br />possible values: ['colored', 'black-white']
		</td>
	</tr>
	<tr>
		<td>colors</td>
		<td>is an array of different colors. These colors are used for the filling of the nodes
			<br /><br />default: a number of colors in the attribute 'default_colorset'
			<br />possible values: any array of colors
		</td>
	</tr>
	<tr>
		<td>nodeSize</td>
		<td>defines if the size of the nodes is based on the number of incoming or outgoing links.
			<br /><br />default: 'outgoing'
			<br />possible values: ['outgoing', 'incoming']
		</td>
	</tr>
	<tr>
	<td>directed</td>
		<td>defines if the network diagram should be directed (true) or undirected (false)
			<br /><br />default: true
			<br />possible values: [true, false]
		</td>
	</tr>
	<tr>
		<td>tooltipSetting</td>
		<td>defines if tooltips should be shown in case of a mouseoverevent
			<br /><br />default: 'static'
			<br />possible values: ['none', 'movable', 'static']
		</td>
	</tr>
	<tr>
		<td>sortingTooltip</td>
		<td>defines by which criteria the connections in the tooltip should be sorted
			<br /><br />default: 'source'
			<br />possible values: ['source', 'target', 'data']
		</td>
	</tr>
	<tr>
		<td>sortingOrderTooltip</td>
		<td>defines if the nodes should be ordered ascending or descending
			<br /><br />default: true
			<br />possible values: [true, false] true means ascending, false means descending
		</td>
	</tr>
	<tr>
		<td>tooltipOrientation</td>
		<td>defines if the text in the tooltip should be horizontal or vertical
			<br /><br />default: 'horizontal'
			<br />possible values: ['horizontal', 'vertical']
		</td>
	</tr>
	<tr>
		<td>onClickNode</td>
		<td>defines a function which should be executed on a click event on a node
			<br /><br />default: null
			<br />possible values: any function
		</td>
	</tr>
	<tr>
		<td>onClickLink</td>
		<td>defines a function which should be executed on a click event on a link
			<br /><br />default: null
			<br />possible values: any function
		</td>
	</tr>
</table>
