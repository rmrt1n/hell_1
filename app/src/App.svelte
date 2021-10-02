<script>
	let imageResult, fileinput, fileName;
	let result

	const onFileSelected =(e)=>{
		let image = e.target.files[0];
		let reader = new FileReader();
			
		reader.readAsDataURL(image);
		console.log(image.type)
		if (image.type != "image/png" && image.type !="image/jpg" && image.type != "image/jpeg") {
			window.alert("Please use .png or .jpg format");
			return false;
		}
		fileName = image.name;

		reader.onload = e => {
			imageResult = e.target.result;
		};
	}
	
	const onSubmit = (e) => {
		let formData = new FormData()
		formData.append('img', e.target['input-file'].files[0])
		if (!e.target['input-file'].files[0]) return;
		fetch('http://localhost:5000/predict', {
			method: 'POST',
			body: formData,
		})
			.then((r) => r.json())
			.then((data) => result = Number((data.result)).toFixed(1))
			.catch((err) => console.log(err))
	}

		const removeFile = () => {
			imageResult = null
		}
</script>


<main>
	<div id="app">
		<div style="padding-left: 2%">
			<h1>CinePoster</h1>
		</div>
		<form on:submit|preventDefault={ onSubmit }>
			<div id="left-container">
				<h1 class="title">See if a movie is worth watching</h1>
				<p class="subtitle">Rate a movie's prospect through it's poster. Simple.</p>
				{#if result}
					<div style="display: flex; align-items: center">
						<h3>Score:  { result }</h3>
					</div>
				{/if}
				<button id="score-btn">score</button>
			</div>

			<div id="right-container">
				{#if imageResult}
					<div style="position: relative;">
						<img id="delete-btn" src="delete.svg" on:click={ removeFile } width="25px" alt=""/>
						<img class="imageResult" src="{imageResult}" alt="poster" />
					</div>
				{:else}
				<!-- <img class="imageResult" src="No-Image-Found.png" alt="" />  -->
					<div id="image-placeholder">
						<img src="upload.svg" alt="upload" width="50"/>
					</div>
				{/if}
					<div class="file-form">
						<input
							id="input-file"
							style="display:none"
							type="file"
							accept=".jpg, .png, .jpeg"
							on:change={(e)=>onFileSelected(e)}
							bind:this={fileinput}
						/>
						<label for="input-file">Select file</label>
					</div>
			</div>
		</form>
	</div>
</main>

<style>
	main {
		height: 100vh;
		display: flex;
		align-items:center;
		justify-content:center;
		background: rgb(2,0,36);
		background: radial-gradient(circle, rgba(2,0,36,1) 0%, rgba(7,42,142,1) 19%, rgba(0,212,255,1) 100%);
	}

	#app {
		width: 95%;
		height: 95%;
		background-color: white;
		border-radius: 10px;
	}

	form {
		display:flex;
		align-items: center;
		justify-content:center;
		height: 100%;
	}
 
	#left-container {
		width: 60%;
		padding: 0 5% 0 5%;
		height: 80%;
		display: flex;
		flex-direction: column;
		justify-content:top;
		position: relative;
	}

	#right-container {
		width: 40%;
		height: 80%;
		padding: 0 5% 0 5%;
		display: flex;
		flex-direction: column;
		align-items: center;
		position: relative;
	}

	#right-container:hover #delete-btn {
		display: block;
	}
	#score-btn {
		position: absolute;
		bottom: 15%;
		background-color: aliceblue;
		border: black solid 1px;
		padding: 10px 30px;
		cursor: pointer;
	}

	#delete-btn {
		display: none;
		position: absolute;
		top: 1%;
		right: 1%;
		cursor: pointer;
	}

	#image-placeholder {
		width: 300px;
		height: 400px;
		background-color: #CBD5E1;
		display: flex;
		align-items: center;
		justify-content: center;
		color: #334155;
		cursor: pointer;
	}

	.file-form{
		display:flex;
		margin: 20px;
		padding: 10px 20px;
		border: 1px solid black;
		cursor: pointer;
		background-color: aliceblue;
	}

	.file-form label{
		cursor: pointer;
	}

	.imageResult{
		display:flex;
		max-width: 300px;
		max-height: 400px;
		height:100%;
		width:100%;
	}

	.title{
		font-size: 40px;
		max-width: 350px;
		width: 100%;
	}
</style>

 
