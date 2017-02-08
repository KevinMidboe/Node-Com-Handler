var button = document.getElementById("btnSearch");

button.onclick = function () {
    var text = document.getElementById("link_id").value;
    console.log(text);
    queryTMDB(text);
}

function clearSearchResults() {
	var displayNode = document.getElementById("display");
	while (displayNode.firstChild) {
    displayNode.removeChild(displayNode.firstChild);
	}
}

function toggle(button) {
	toggleNode = document.getElementById("myonoffswitch");
	console.log(toggleNode);


  if(toggleNode.value=="movies"){
   toggleNode.value="shows";}

  else if(toggleNode.value=="shows"){
   toggleNode.value="movies";}
}

function queryTMDB(query) {
	var data = "{}";

	var xhr = new XMLHttpRequest();
	xhr.withCredentials = true;

	xhr.addEventListener("readystatechange", function () {
	  if (this.readyState === this.DONE) {
	  	clearSearchResults()

	  	var display = document.getElementById("display");
	  	var jsonObj = JSON.parse(this.responseText);
	  	console.log(jsonObj.movies);

	  	Object.keys(jsonObj.movies).forEach(function(key) {
	  		var id = jsonObj.movies[key].id;
	  		var title = jsonObj.movies[key].title;

	  		var posterURL = jsonObj.movies[key].poster_path;
	  		if (posterURL != null)
	  			var poster_path = "http://image.tmdb.org/t/p/w500"+jsonObj.movies[key].poster_path;
	  		else
	  			var poster_path = "images/image_nf.svg";

	  		var exists = jsonObj.movies[key].exists;
	  		
	  		var node = document.createElement("li");                 // Create a <li> node
			var imageNode = document.createElement('img');
			var textNode = document.createTextNode(title);         // Create a text node
			var buttonNode = document.createElement("span");
			var button2Node = document.createElement("span");
			if (!exists) {
				buttonNode.innerHTML = '<button onclick="request('+ id +')">REQUEST</button>';
			}
			else
				button2Node.innerHTML = '<button onclick="request('+ id +')">FORCE REQUEST</button>';
			
			imageNode.src = poster_path;
			imageNode.style.width = "500px";

			node.appendChild(textNode);       	                    // Append the text to <li>
			node.appendChild(imageNode);
			node.appendChild(buttonNode);
			node.appendChild(button2Node);

			display.appendChild(node);

	  	});
	  }
	  else {
	  	console.log("404");
	  }
	});

	xhr.open("GET", "http://localhost:63590/api/v1/plex/request?query="+query);

	console.log(data);
	xhr.send(data);
}