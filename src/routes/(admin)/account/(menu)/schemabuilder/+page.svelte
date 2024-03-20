<script>
  /** @type {import('./$types').PageData} */
  export let data
  let inputs = [{ id: 1, value: "" }]
  let refs = []
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
  <div class="card-body">
    {#each inputs as input (input.id)}
      <div class="flex items-center gap-2">
        <label class="input input-bordered flex items-center gap-2">
          <input type="text" class="grow" placeholder="Field Name" bind:value={input.value} />
        </label>
        <label class="input input-bordered flex items-center gap-2">
          <input type="text" class="grow" placeholder="Description" />
        </label>
        <button class="btn btn-outline btn-primary">Add Field</button>
      </div>
    {/each}
  </div>
</div>
