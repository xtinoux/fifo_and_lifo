function DisplayListeSection(ListeLycee) {
	// document.getElementById("demo").innerHTML = "ok";
	lyceechosen = getSelectedLycee();
	var ListeSection = new Array(ListeLycee[1][lyceechosen].length);
	for (var i = ListeLycee[1][lyceechosen].length - 1; i >= 0; i--) {
		ListeSection[i] = ListeLycee[1][lyceechosen][i];
	};
	defRadioSection(ListeSection);
}

function getSelectedLycee() {
	var radios = document.getElementsByName("lycee");
	for(var i = 0; i < radios.length; i++){
		if(radios[i].checked) {
			return i;
		}
	}
}

function defRadioSection (ListeSection) {
	var debut = ListeSection.length-1;//ListeSection.length-1;
	// document.getElementById("demo").innerHTML = ListeSection.length;
	var label = document.createElement("label");
	label.setAttribute("for", "radio"+ListeSection[debut]);
	label.setAttribute("id", "label"+ListeSection[debut]);
	var labeltext = document.createTextNode(ListeSection[debut]);
	label.appendChild(labeltext);
	document.getElementById("formsection").insertBefore(label,document.getElementById("first-el"));
	
	var radio = document.createElement("input");
	radio.setAttribute("type", "radio");
	radio.setAttribute("name", "section");
	radio.setAttribute("id", "radio"+ListeSection[debut]);
	radio.setAttribute("onclick","disablePasswd()")
	document.getElementById("formsection").insertBefore(radio,document.getElementById("label"+ListeSection[debut]));

	for (var i = ListeSection.length-2; i >= 0; i--) {		
		var label = document.createElement("label");
		label.setAttribute("for", ListeSection[i]);
		label.setAttribute("id", "label"+ListeSection[i]);
		var labeltext = document.createTextNode(ListeSection[i]);
		label.appendChild(labeltext);
		document.getElementById("formsection").insertBefore(label,document.getElementById("radio"+ListeSection[i-1]));

		var radio = document.createElement("input");
		radio.setAttribute("type", "radio");
		radio.setAttribute("name", "section");
		radio.setAttribute("id", ListeSection[i]);
		radio.setAttribute("onclick","disablePasswd()")
		document.getElementById("formsection").insertBefore(radio,document.getElementById("label"+ListeSection[i]));
	};
}

function disablePasswd() {
	document.getElementById("passwd").disabled = false;
}