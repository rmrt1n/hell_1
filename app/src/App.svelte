<script>
	let imageResult, fileinput, fileName;
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
	
</script>


<div id="app">
		<h1>Upload Image</h1>
        {#if imageResult}
        <img class="imageResult" src="{imageResult}" alt="d" />
        {:else}
        <img class="imageResult" src="No-Image-Found.png" alt="" /> 
        {/if}
		<div class="file-form">
			<input id="input-file" style="display:none" type="file" accept=".jpg, .png, .jpeg" on:change={(e)=>onFileSelected(e)} bind:this={fileinput}>
			<label for="input-file">Select file</label>
		</div>
		{#if fileName}
			<p>
				{fileName}
			</p>
		{/if}
</div>

<style>
	#app{
		display:flex;
		align-items:center;
		justify-content:center;
		flex-flow:column;
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
		max-height: 300px;
		height:100%;
		width:100%;
	}
</style>

 