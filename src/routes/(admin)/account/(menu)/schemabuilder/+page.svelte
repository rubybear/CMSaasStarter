<script>
  /** @type {import('./$types').PageData} */
  export let data
  let inputs = [{ id: 1, name: "", description: "" }]
  let labelText = "Section Name"

  function addField() {
    const newId = inputs.length + 1
    inputs = [...inputs, { id: newId, name: "", description: "" }]
  }

  function submitSchema() {
    // Implement your logic to submit the schema data (inputs array)
    console.log("Schema submitted:", inputs)
  }
</script>

<svelte:head>
  <title>Schema Builder</title>
  <meta
    name="description"
    content="Define the schema for the document extraction"
  />
</svelte:head>

<div class="card card-side bg-base-100 shadow-xl">
  <figure>
    <img
      src="https://textractdevdata.s3.amazonaws.com/sampleform.png?AWSAccessKeyId=AKIA6A5YN6FCO7XLY2YC&Expires=1710625321&Signature=pjaY9iyKd5DTjEdOBEiB6UgVG2o%3D"
      alt="Movie"
    />
  </figure>
  <div class="card-body p-4 flex flex-col items-stretch gap-4">
    {#each inputs as input (input.id)}
      <div class="flex items-center gap-2">
        <label class="input input-bordered w-full flex items-center gap-2">
          <input
            type="text"
            class="w-full"
            placeholder="Section Name"
            bind:value={input.name}
          />
        </label>
        <label class="input input-bordered w-full flex items-center gap-2">
          <input
            type="text"
            class="w-full"
            placeholder="Field Name"
            bind:value={input.name}
          />
        </label>
        <label class="input input-bordered w-full flex items-center gap-2">
          <input
            type="text"
            class="w-full"
            placeholder="Description"
            bind:value={input.description}
          />
          Section Name</label
        >
      </div>
    {/each}
    <button class="btn btn-primary" on:click={addField}> Add Field </button>
    <div>
      <label
        for="price"
        class="block text-sm font-medium leading-6 text-gray-900"
        >{labelText}</label
      >
      <div class="relative mt-2 rounded-md shadow-sm">
        <input
          type="text"
          name="price"
          id="price"
          class="input input-bordered w-full flex items-center gap-2"
          placeholder="Field Name"
          bind:value={labelText}
        />
      </div>
      <button class="btn btn-primary">Add Field</button>
    </div>
    <button
      class="btn btn-success absolute bottom-4 right-4"
      on:click={submitSchema}
    >
      Submit Schema
    </button>
  </div>
</div>
